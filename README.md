# FPL Auction System

A real-time web application for running Fantasy Premier League player auctions with friends. This system replaces manual spreadsheet-based auctions with an automated, mobile-friendly platform.

## Features

- **Real-time Bidding**: Live auction system with countdown timers
- **Squad Validation**: Automatic enforcement of FPL rules (positions, club limits, budgets)
- **Mobile-First Design**: Optimized for use during social gatherings
- **Turn-Based System**: Fair nomination system with automatic progression
- **Live Updates**: All participants see bids and squad changes instantly
- **Game Management**: Chairman controls for pause/resume functionality

## Tech Stack

### Frontend
- Next.js 14 (App Router)
- TypeScript
- Tailwind CSS + shadcn/ui
- Socket.io Client
- Zustand (State Management)
- React Query

### Backend
- Node.js + Express
- TypeScript
- Socket.io
- PostgreSQL + Prisma ORM
- JWT Authentication

## Getting Started

### Prerequisites

- Node.js 18+
- PostgreSQL database
- npm or yarn

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd fpl-auction
```

2. Install dependencies:

**Frontend:**
```bash
cd frontend
npm install
```

**Backend:**
```bash
cd backend
npm install
```

3. Set up environment variables:

**Backend (.env):**
```env
DATABASE_URL="postgresql://username:password@localhost:5432/fpl_auction"
PORT=5000
NODE_ENV=development
FRONTEND_URL=http://localhost:3000
JWT_SECRET=your-secret-key
```

**Frontend (.env.local):**
```env
NEXT_PUBLIC_API_URL=http://localhost:5000
NEXT_PUBLIC_WS_URL=ws://localhost:5000
```

4. Set up the database:
```bash
cd backend
npx prisma generate
npx prisma migrate dev
```

5. Start the development servers:

**Backend:**
```bash
npm run dev
```

**Frontend:**
```bash
npm run dev
```

## Usage

### Admin Setup

1. Navigate to `/admin` to access the admin dashboard
2. Create a new season (e.g., "2024/25")
3. Import players via CSV file with format: `code,name,club,position`
4. Activate the season

### Running an Auction

1. **Create Game**: Navigate to home page and click "Create New Game"
2. **Share Code**: Share the generated game code with participants
3. **Join Game**: Participants join using the code and enter their details
4. **Start Auction**: Chairman (first to join) starts the game
5. **Nominate**: Players take turns nominating players
6. **Bid**: Eligible managers bid on nominated players
7. **Build Squad**: Continue until all managers have 15 players

### Game Rules

- **Squad Size**: 15 players per manager
- **Positions**: 2 GK, 5 DEF, 5 MID, 3 FWD
- **Club Limit**: Maximum 2 players from any Premier League club
- **Budget**: £200m per manager (configurable)
- **Bidding**: 30-second initial countdown, resets to 10 seconds on new bids

## Development

### Project Structure

```
fpl-auction/
├── frontend/          # Next.js frontend application
│   ├── app/          # App router pages
│   │   ├── components/   # React components
│   │   ├── hooks/       # Custom React hooks
│   │   ├── lib/         # Utilities
│   │   └── stores/      # Zustand stores
│   └── public/         # Static assets
│
└── backend/           # Express backend application
    ├── src/
    │   ├── routes/      # API routes
    │   ├── socket/      # Socket.io handlers
    │   ├── engine/      # Game logic
    │   ├── types/       # TypeScript types
    │   └── utils/       # Utilities
    └── prisma/          # Database schema
```

### Key Components

- **AuctionEngine**: Core game logic for nominations, bidding, and validation
- **Socket Handlers**: Real-time event management
- **Game State**: Centralized state management for active games
- **Validation System**: Ensures all FPL rules are enforced

## Deployment

### Frontend (Vercel)
1. Connect GitHub repository to Vercel
2. Set environment variables
3. Deploy with automatic builds

### Backend (Railway/Render)
1. Deploy PostgreSQL database
2. Deploy Node.js application
3. Configure environment variables
4. Set up WebSocket support

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

MIT License

## Support

For issues and feature requests, please use the GitHub issue tracker. 