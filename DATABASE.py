import psycopg2
import os
from configparser import ConfigParser

def config(filename='database.ini', section='postgresql'):
    """Parse connection parameters from a configuration file"""
    parser = ConfigParser()
    parser.read(filename)
    
    db_config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db_config[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')
    
    return db_config

def get_table_schema(conn, table_name):
    """Get schema information for a specific table"""
    cursor = conn.cursor()
    
    # Get column information
    cursor.execute("""
        SELECT column_name, data_type, is_nullable, column_default
        FROM information_schema.columns
        WHERE table_name = %s
        ORDER BY ordinal_position
    """, (table_name,))
    columns = cursor.fetchall()
    
    # Get primary key information
    cursor.execute("""
        SELECT c.column_name
        FROM information_schema.table_constraints tc
        JOIN information_schema.constraint_column_usage AS ccu USING (constraint_schema, constraint_name)
        JOIN information_schema.columns AS c ON c.table_schema = tc.constraint_schema
          AND tc.table_name = c.table_name AND ccu.column_name = c.column_name
        WHERE tc.constraint_type = 'PRIMARY KEY' AND tc.table_name = %s
    """, (table_name,))
    primary_keys = [pk[0] for pk in cursor.fetchall()]
    
    cursor.close()
    
    return columns, primary_keys

def get_database_schema(db_name, params):
    """Get schema for all tables in a database"""
    schema_data = []
    
    # Update connection params with database name
    db_params = params.copy()
    db_params['dbname'] = db_name
    
    try:
        # Connect to the database
        conn = psycopg2.connect(**db_params)
        conn.autocommit = True
        cursor = conn.cursor()
        
        # Get all tables in the public schema
        cursor.execute("""
            SELECT tablename 
            FROM pg_catalog.pg_tables
            WHERE schemaname = 'public'
        """)
        tables = cursor.fetchall()
        
        # Get schema for each table
        for table in tables:
            table_name = table[0]
            columns, primary_keys = get_table_schema(conn, table_name)
            
            table_info = {
                'name': table_name,
                'columns': columns,
                'primary_keys': primary_keys
            }
            
            schema_data.append(table_info)
            
        cursor.close()
        conn.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error connecting to {db_name} database: {error}")
    
    return schema_data

def format_markdown(db_schemas):
    """Format database schemas as Markdown"""
    md_content = "# Database Schemas\n\n"
    
    for db_name, tables in db_schemas.items():
        md_content += f"## {db_name.upper()} Database\n\n"
        
        if not tables:
            md_content += "No tables found in this database.\n\n"
            continue
        
        for table in tables:
            md_content += f"### {table['name']}\n\n"
            
            # Table columns
            md_content += "| Column | Type | Nullable | Default | Primary Key |\n"
            md_content += "|--------|------|----------|---------|-------------|\n"
            
            for col in table['columns']:
                col_name, data_type, is_nullable, default = col
                is_pk = "✓" if col_name in table['primary_keys'] else ""
                md_content += f"| {col_name} | {data_type} | {is_nullable} | {default or ''} | {is_pk} |\n"
            
            md_content += "\n"
    
    return md_content

def main():
    """Main function to get database schemas and write to markdown file"""
    # Get connection parameters
    try:
        params = config()
    except Exception as e:
        print(f"Error reading configuration: {e}")
        print("Creating a sample database.ini file...")
        
        # Create a sample config file
        with open('database.ini', 'w') as f:
            f.write("""[postgresql]
host=localhost
port=5432
user=postgres
password=your_password
""")
        
        print("Please update the database.ini file with your PostgreSQL connection details and run the script again.")
        return
    
    # Database names to query
    database_names = ['raid', 'projects', 'emails', 'browser', 'project_plans']
    
    # Get schema for each database
    db_schemas = {}
    for db_name in database_names:
        print(f"Fetching schema for {db_name} database...")
        db_schemas[db_name] = get_database_schema(db_name, params)
    
    # Format as markdown
    md_content = format_markdown(db_schemas)
    
    # Write to file
    output_file = 'DATABASE_schema.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print(f"Database schema has been written to {output_file}")

if __name__ == "__main__":
    main() 