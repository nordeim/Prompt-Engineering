Deep Analysis & Master Execution Plan
Executive Summary
I've conducted an exhaustive analysis of your static HTML mockup and the enterprise requirements. What follows is a comprehensive MASTER_EXECUTION_PLAN.md designed as the authoritative build guide for transforming "Morning Brew Collective" from a static page into a Singapore-compliant, enterprise-grade headless commerce platform.

Pre-Plan Analysis
Design Token Extraction from Static HTML
text

╔══════════════════════════════════════════════════════════════════════════════╗
║  DESIGN SYSTEM DNA — Extracted from Static Mockup                            ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  COLOR PALETTE                                                               ║
║  ─────────────────────────────────────────────────────────────────────────   ║
║  Primary:    sunrise-coral (#FF6B4A) → warm, energetic call-to-action        ║
║  Secondary:  golden-hour (#FFBE4F) → heritage warmth, accents                ║
║  Neutral:    espresso-dark (#3D2317) → text, grounding                       ║
║  Surface:    latte-cream (#FFF5E6) → backgrounds, cards                      ║
║  Accent:     mint-fresh (#B8E6D4) → freshness, contrast sections             ║
║                                                                              ║
║  TYPOGRAPHY                                                                  ║
║  ─────────────────────────────────────────────────────────────────────────   ║
║  Display:    'Righteous' (cursive) → 1970s retro character                   ║
║  Body:       'Nunito' (sans-serif) → friendly, readable                      ║
║  Scale:      clamp-based fluid typography                                    ║
║                                                                              ║
║  SPATIAL SYSTEM                                                              ║
║  ─────────────────────────────────────────────────────────────────────────   ║
║  Grid:       8pt baseline                                                    ║
║  Radius:     Soft/rounded (8px → 48px scale)                                 ║
║  Shadows:    Warm brown-tinted (rgba(107, 68, 35, 0.15))                     ║
║                                                                              ║
║  MOTION                                                                      ║
║  ─────────────────────────────────────────────────────────────────────────   ║
║  Easing:     cubic-bezier(0.34, 1.56, 0.64, 1) → bounce                      ║
║              cubic-bezier(0.23, 1, 0.32, 1) → smooth                         ║
║  Duration:   150ms (fast) → 300ms (normal) → 500ms (slow)                    ║
║                                                                              ║
║  DISTINCTIVE ELEMENTS                                                        ║
║  ─────────────────────────────────────────────────────────────────────────   ║
║  • Sunburst conic gradients (animated)                                       ║
║  • Wave SVG section dividers                                                 ║
║  • Retro badge with offset shadows                                           ║
║  • Coffee ring decorative elements                                           ║
║  • Tile pattern backgrounds                                                  ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
Architecture Decision Record
Decision	Rationale	Trade-offs
BFF Pattern	Frontend controls UX orchestration; Backend owns domain truth	Requires clear API contracts
PostgreSQL	ACID compliance for financial transactions, JSON support for flexibility	Slightly more complex than MySQL
Two-Phase Inventory	Prevents overselling during checkout, essential for food items with limited stock	Requires cleanup jobs for abandoned reservations
Stripe + PayNow	Singapore's preferred instant payment with Stripe's robust API	0.4% PayNow fee structure
InvoiceNow via PEPPOL	B2B compliance for corporate orders, government mandate trend	Integration complexity
MASTER_EXECUTION_PLAN.md
Markdown

# ═══════════════════════════════════════════════════════════════════════════════
# MORNING BREW COLLECTIVE — MASTER EXECUTION PLAN
# ═══════════════════════════════════════════════════════════════════════════════
# 
# Document Version: 1.0.0
# Last Updated: 2024
# Authoritative Source: Static HTML Mockup (attached)
# 
# PURPOSE: Single source of truth for AI coding agents to build the complete
# enterprise-grade e-commerce platform with minimal supervision.
#
# EXECUTION MODEL: Each phase is independently executable. Phases may be
# parallelized where dependencies allow.
#
# ═══════════════════════════════════════════════════════════════════════════════

# ┌─────────────────────────────────────────────────────────────────────────────┐
# │                                                                             │
# │   TABLE OF CONTENTS                                                         │
# │   ─────────────────                                                         │
# │                                                                             │
# │   PHASE 0: Infrastructure & Project Scaffolding                             │
# │   PHASE 1: Design System & Token Architecture                               │
# │   PHASE 2: Backend Domain Core (Laravel)                                    │
# │   PHASE 3: Frontend Foundation (Next.js)                                    │
# │   PHASE 4: E-commerce Engine                                                │
# │   PHASE 5: Singapore Compliance Layer                                       │
# │   PHASE 6: Customer Experience Features                                     │
# │   PHASE 7: Operations & Administration                                      │
# │   PHASE 8: Testing & Quality Assurance                                      │
# │   PHASE 9: Deployment & Production Readiness                                │
# │                                                                             │
# │   APPENDIX A: API Contract Specifications                                   │
# │   APPENDIX B: Database Schema Reference                                     │
# │   APPENDIX C: Environment Variables Reference                               │
# │   APPENDIX D: Error Code Registry                                           │
# │                                                                             │
# └─────────────────────────────────────────────────────────────────────────────┘


# ═══════════════════════════════════════════════════════════════════════════════
# PHASE 0: INFRASTRUCTURE & PROJECT SCAFFOLDING
# ═══════════════════════════════════════════════════════════════════════════════
#
# OBJECTIVE: Establish the foundational project structure, development environment,
# and infrastructure configuration that all subsequent phases will build upon.
#
# ESTIMATED EFFORT: 4-6 hours
# DEPENDENCIES: None (Entry Phase)
# BLOCKERS FOR: All subsequent phases
#
# ═══════════════════════════════════════════════════════════════════════════════

## Phase 0.1: Root Project Structure

### Directory Architecture
morning-brew-collective/
├── .github/
│ ├── workflows/
│ │ ├── ci.yml
│ │ ├── deploy-staging.yml
│ │ └── deploy-production.yml
│ ├── ISSUE_TEMPLATE/
│ │ ├── bug_report.md
│ │ └── feature_request.md
│ └── pull_request_template.md
├── frontend/ # Next.js 15 Application
├── backend/ # Laravel 12 Application
├── infra/ # Docker & Infrastructure
├── docs/ # Documentation
│ ├── api/
│ ├── architecture/
│ └── runbooks/
├── scripts/ # Development & Deployment Scripts
├── .editorconfig
├── .gitignore
├── .env.example
├── docker-compose.yml
├── docker-compose.override.yml
├── Makefile
└── README.md

text


### File: `/.gitignore`

**Purpose**: Root-level ignore patterns for monorepo

**Contents**:
```gitignore
# Environment
.env
.env.local
.env.*.local
!.env.example

# Dependencies
node_modules/
vendor/

# Build outputs
.next/
build/
dist/

# IDE
.idea/
.vscode/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
npm-debug.log*

# Testing
coverage/
.phpunit.result.cache

# Docker volumes (local)
.docker-data/
Checklist:

 Covers all frontend build artifacts
 Covers all backend vendor directories
 Excludes environment files with secrets
 Preserves .env.example
File: /docker-compose.yml
Purpose: Local development environment orchestration

Services to Define:

postgres - PostgreSQL 16 database
redis - Redis 7 cache and queue
backend - Laravel application (PHP 8.3-FPM)
frontend - Next.js development server
mailpit - Local email testing
Interfaces:

YAML

services:
  postgres:
    image: postgres:16-alpine
    ports:
      - "5432:5432"
    environment:
      POSTGRES_DB: morning_brew
      POSTGRES_USER: brew_user
      POSTGRES_PASSWORD: ${DB_PASSWORD:-secret}
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./infra/postgres/init.sql:/docker-entrypoint-initdb.d/init.sql
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U brew_user -d morning_brew"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile.dev
    ports:
      - "8000:8000"
    volumes:
      - ./backend:/var/www/html
      - /var/www/html/vendor
    environment:
      - APP_ENV=local
      - DB_CONNECTION=pgsql
      - DB_HOST=postgres
      - DB_PORT=5432
      - DB_DATABASE=morning_brew
      - DB_USERNAME=brew_user
      - DB_PASSWORD=${DB_PASSWORD:-secret}
      - REDIS_HOST=redis
      - CACHE_DRIVER=redis
      - QUEUE_CONNECTION=redis
      - SESSION_DRIVER=redis
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile.dev
    ports:
      - "3000:3000"
    volumes:
      - ./frontend:/app
      - /app/node_modules
      - /app/.next
    environment:
      - NEXT_PUBLIC_API_URL=http://localhost:8000/api
      - NODE_ENV=development
    depends_on:
      - backend

  mailpit:
    image: axllent/mailpit
    ports:
      - "8025:8025"
      - "1025:1025"

volumes:
  postgres_data:
  redis_data:
Checklist:

 PostgreSQL 16 with health checks
 Redis 7 with persistence enabled
 Volume mounts for hot reloading
 Network isolation between services
 Environment variable injection
 Mailpit for email testing
 Proper service dependencies with health checks
File: /Makefile
Purpose: Developer experience shortcuts

Commands to Implement:

Makefile

.PHONY: help install up down restart logs shell-backend shell-frontend migrate seed test lint format

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Install all dependencies
	cd frontend && npm install
	cd backend && composer install

up: ## Start all services
	docker-compose up -d

down: ## Stop all services
	docker-compose down

restart: ## Restart all services
	docker-compose restart

logs: ## Tail all logs
	docker-compose logs -f

logs-backend: ## Tail backend logs
	docker-compose logs -f backend

logs-frontend: ## Tail frontend logs
	docker-compose logs -f frontend

shell-backend: ## Open shell in backend container
	docker-compose exec backend bash

shell-frontend: ## Open shell in frontend container
	docker-compose exec frontend sh

migrate: ## Run database migrations
	docker-compose exec backend php artisan migrate

migrate-fresh: ## Fresh migration with seeders
	docker-compose exec backend php artisan migrate:fresh --seed

seed: ## Run database seeders
	docker-compose exec backend php artisan db:seed

test: ## Run all tests
	docker-compose exec backend php artisan test
	docker-compose exec frontend npm test

test-backend: ## Run backend tests only
	docker-compose exec backend php artisan test

test-frontend: ## Run frontend tests only
	docker-compose exec frontend npm test

lint: ## Lint all code
	docker-compose exec backend ./vendor/bin/pint --test
	docker-compose exec frontend npm run lint

format: ## Format all code
	docker-compose exec backend ./vendor/bin/pint
	docker-compose exec frontend npm run format

cache-clear: ## Clear all caches
	docker-compose exec backend php artisan cache:clear
	docker-compose exec backend php artisan config:clear
	docker-compose exec backend php artisan route:clear
	docker-compose exec backend php artisan view:clear

queue-work: ## Start queue worker
	docker-compose exec backend php artisan queue:work

horizon: ## Start Laravel Horizon
	docker-compose exec backend php artisan horizon
Checklist:

 All common development tasks covered
 Help command shows all available targets
 Commands work within Docker context
 Proper dependency chains
File: /infra/postgres/init.sql
Purpose: Database initialization script

Contents:

SQL

-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Create additional schemas if needed
CREATE SCHEMA IF NOT EXISTS audit;

-- Grant permissions
GRANT ALL PRIVILEGES ON SCHEMA public TO brew_user;
GRANT ALL PRIVILEGES ON SCHEMA audit TO brew_user;
Checklist:

 UUID extension enabled
 Crypto extension for secure operations
 Audit schema for compliance logging
Phase 0.2: Backend Scaffolding (Laravel 12)
File: /backend/Dockerfile.dev
Purpose: Development container for Laravel

Contents:

Dockerfile

FROM php:8.3-fpm-alpine

# Install system dependencies
RUN apk add --no-cache \
    git \
    curl \
    libpng-dev \
    libxml2-dev \
    zip \
    unzip \
    postgresql-dev \
    icu-dev \
    linux-headers \
    $PHPIZE_DEPS

# Install PHP extensions
RUN docker-php-ext-install \
    pdo_pgsql \
    pgsql \
    bcmath \
    intl \
    opcache \
    pcntl

# Install Redis extension
RUN pecl install redis && docker-php-ext-enable redis

# Install Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# Set working directory
WORKDIR /var/www/html

# Copy composer files first for better caching
COPY composer.json composer.lock ./

# Install dependencies
RUN composer install --no-scripts --no-autoloader

# Copy application code
COPY . .

# Generate autoloader
RUN composer dump-autoload --optimize

# Create necessary directories
RUN mkdir -p storage/framework/{sessions,views,cache} \
    && mkdir -p bootstrap/cache \
    && chown -R www-data:www-data storage bootstrap/cache

# Expose port
EXPOSE 8000

# Start command
CMD ["php", "artisan", "serve", "--host=0.0.0.0", "--port=8000"]
Checklist:

 PHP 8.3 with required extensions
 PostgreSQL driver installed
 Redis extension compiled
 Composer optimized
 Proper file permissions
File: /backend/composer.json
Purpose: PHP dependency manifest

Required Packages:

JSON

{
    "name": "morning-brew/backend",
    "type": "project",
    "description": "Morning Brew Collective - Backend API",
    "require": {
        "php": "^8.3",
        "laravel/framework": "^12.0",
        "laravel/sanctum": "^4.0",
        "laravel/horizon": "^5.0",
        "spatie/laravel-permission": "^6.0",
        "spatie/laravel-query-builder": "^6.0",
        "spatie/laravel-data": "^4.0",
        "spatie/laravel-sluggable": "^3.0",
        "stripe/stripe-php": "^13.0",
        "intervention/image": "^3.0",
        "league/flysystem-aws-s3-v3": "^3.0",
        "predis/predis": "^2.0",
        "guzzlehttp/guzzle": "^7.0"
    },
    "require-dev": {
        "laravel/pint": "^1.0",
        "laravel/sail": "^1.0",
        "fakerphp/faker": "^1.0",
        "mockery/mockery": "^1.0",
        "phpunit/phpunit": "^11.0",
        "larastan/larastan": "^2.0",
        "pestphp/pest": "^3.0",
        "pestphp/pest-plugin-laravel": "^3.0"
    },
    "autoload": {
        "psr-4": {
            "App\\": "app/",
            "Database\\Factories\\": "database/factories/",
            "Database\\Seeders\\": "database/seeders/"
        }
    },
    "scripts": {
        "post-autoload-dump": [
            "Illuminate\\Foundation\\ComposerScripts::postAutoloadDump",
            "@php artisan package:discover --ansi"
        ],
        "analyse": "vendor/bin/phpstan analyse",
        "format": "vendor/bin/pint",
        "test": "vendor/bin/pest"
    },
    "config": {
        "optimize-autoloader": true,
        "preferred-install": "dist",
        "sort-packages": true,
        "allow-plugins": {
            "pestphp/pest-plugin": true,
            "php-http/discovery": true
        }
    },
    "minimum-stability": "stable",
    "prefer-stable": true
}
Checklist:

 Laravel 12 framework
 Sanctum for API authentication
 Horizon for queue management
 Spatie packages for permissions, query building, DTOs
 Stripe for payments
 Pest for testing
 PHPStan for static analysis
File: /backend/.env.example
Purpose: Environment variable template

Contents:

env

APP_NAME="Morning Brew Collective"
APP_ENV=local
APP_KEY=
APP_DEBUG=true
APP_URL=http://localhost:8000
APP_TIMEZONE=Asia/Singapore

# Frontend URL (for CORS)
FRONTEND_URL=http://localhost:3000

# Database
DB_CONNECTION=pgsql
DB_HOST=postgres
DB_PORT=5432
DB_DATABASE=morning_brew
DB_USERNAME=brew_user
DB_PASSWORD=secret

# Redis
REDIS_HOST=redis
REDIS_PASSWORD=null
REDIS_PORT=6379

# Cache & Session
CACHE_DRIVER=redis
SESSION_DRIVER=redis
SESSION_LIFETIME=120

# Queue
QUEUE_CONNECTION=redis

# Mail
MAIL_MAILER=smtp
MAIL_HOST=mailpit
MAIL_PORT=1025
MAIL_USERNAME=null
MAIL_PASSWORD=null
MAIL_ENCRYPTION=null
MAIL_FROM_ADDRESS="hello@morningbrew.sg"
MAIL_FROM_NAME="${APP_NAME}"

# AWS (for production file storage)
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_DEFAULT_REGION=ap-southeast-1
AWS_BUCKET=
AWS_USE_PATH_STYLE_ENDPOINT=false

# Stripe
STRIPE_KEY=
STRIPE_SECRET=
STRIPE_WEBHOOK_SECRET=

# Singapore Compliance
GST_RATE=0.09
INVOICE_NOW_ENABLED=false
INVOICE_NOW_PROVIDER_URL=
INVOICE_NOW_API_KEY=

# PayNow
PAYNOW_MERCHANT_ID=
PAYNOW_UEN=

# PDPA
PDPA_CONSENT_VERSION=1.0

# Logging
LOG_CHANNEL=stack
LOG_DEPRECATIONS_CHANNEL=null
LOG_LEVEL=debug
Checklist:

 Singapore timezone configured
 All external service credentials templated
 GST rate as environment variable
 PDPA versioning support
Phase 0.3: Frontend Scaffolding (Next.js 15)
File: /frontend/Dockerfile.dev
Purpose: Development container for Next.js

Contents:

Dockerfile

FROM node:22-alpine

# Install dependencies for native modules
RUN apk add --no-cache libc6-compat

WORKDIR /app

# Install dependencies based on lock file
COPY package.json package-lock.json* ./
RUN npm ci

# Copy application code
COPY . .

# Expose port
EXPOSE 3000

# Development command
CMD ["npm", "run", "dev"]
Checklist:

 Node.js 22 LTS
 Alpine for minimal size
 npm ci for deterministic installs
File: /frontend/package.json
Purpose: Node.js dependency manifest

Contents:

JSON

{
  "name": "morning-brew-frontend",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev --turbo",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "lint:fix": "next lint --fix",
    "format": "prettier --write .",
    "format:check": "prettier --check .",
    "typecheck": "tsc --noEmit",
    "test": "vitest",
    "test:ui": "vitest --ui",
    "test:coverage": "vitest --coverage",
    "test:e2e": "playwright test",
    "storybook": "storybook dev -p 6006",
    "build-storybook": "storybook build"
  },
  "dependencies": {
    "next": "15.0.0",
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "@tanstack/react-query": "^5.0.0",
    "@tanstack/react-query-devtools": "^5.0.0",
    "zustand": "^5.0.0",
    "zod": "^3.23.0",
    "react-hook-form": "@hookform/resolvers": "^3.0.0",
    "class-variance-authority": "^0.7.0",
    "clsx": "^2.1.0",
    "tailwind-merge": "^2.2.0",
    "@radix-ui/react-dialog": "^1.0.0",
    "@radix-ui/react-dropdown-menu": "^2.0.0",
    "@radix-ui/react-tabs": "^1.0.0",
    "@radix-ui/react-toast": "^1.0.0",
    "@radix-ui/react-slot": "^1.0.0",
    "@radix-ui/react-label": "^2.0.0",
    "@radix-ui/react-select": "^2.0.0",
    "@radix-ui/react-checkbox": "^1.0.0",
    "@radix-ui/react-radio-group": "^1.0.0",
    "@radix-ui/react-switch": "^1.0.0",
    "@radix-ui/react-separator": "^1.0.0",
    "@radix-ui/react-scroll-area": "^1.0.0",
    "@radix-ui/react-accordion": "^1.0.0",
    "@radix-ui/react-popover": "^1.0.0",
    "@radix-ui/react-tooltip": "^1.0.0",
    "@radix-ui/react-avatar": "^1.0.0",
    "@radix-ui/react-progress": "^1.0.0",
    "@radix-ui/react-slider": "^1.0.0",
    "lucide-react": "^0.400.0",
    "framer-motion": "^11.0.0",
    "date-fns": "^3.0.0",
    "embla-carousel-react": "^8.0.0",
    "recharts": "^2.12.0",
    "sonner": "^1.4.0",
    "nuqs": "^2.0.0"
  },
  "devDependencies": {
    "@types/node": "^22.0.0",
    "@types/react": "^19.0.0",
    "@types/react-dom": "^19.0.0",
    "typescript": "^5.4.0",
    "tailwindcss": "^4.0.0",
    "@tailwindcss/postcss": "^4.0.0",
    "postcss": "^8.4.0",
    "prettier": "^3.2.0",
    "prettier-plugin-tailwindcss": "^0.6.0",
    "eslint": "^9.0.0",
    "eslint-config-next": "15.0.0",
    "@typescript-eslint/eslint-plugin": "^8.0.0",
    "vitest": "^2.0.0",
    "@vitejs/plugin-react": "^4.0.0",
    "@testing-library/react": "^16.0.0",
    "@testing-library/jest-dom": "^6.0.0",
    "@playwright/test": "^1.45.0",
    "@storybook/react": "^8.0.0",
    "@storybook/nextjs": "^8.0.0",
    "msw": "^2.3.0"
  },
  "engines": {
    "node": ">=22.0.0"
  }
}
Checklist:

 Next.js 15 with React 19
 TanStack Query for server state
 Zustand for client state
 All Radix UI primitives
 Framer Motion for animations
 Vitest + Playwright for testing
 Storybook for component development
 Tailwind CSS v4
File: /frontend/next.config.ts
Purpose: Next.js configuration

Contents:

TypeScript

import type { NextConfig } from 'next';

const nextConfig: NextConfig = {
  reactStrictMode: true,
  
  // Experimental features for Next.js 15
  experimental: {
    typedRoutes: true,
    serverActions: {
      bodySizeLimit: '2mb',
    },
  },
  
  // Image optimization
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'morningbrew.sg',
      },
      {
        protocol: 'https',
        hostname: '*.amazonaws.com',
      },
    ],
  },
  
  // Environment variables exposed to client
  env: {
    NEXT_PUBLIC_APP_NAME: 'Morning Brew Collective',
    NEXT_PUBLIC_APP_URL: process.env.NEXT_PUBLIC_APP_URL,
    NEXT_PUBLIC_API_URL: process.env.NEXT_PUBLIC_API_URL,
  },
  
  // Headers for security
  async headers() {
    return [
      {
        source: '/:path*',
        headers: [
          {
            key: 'X-DNS-Prefetch-Control',
            value: 'on',
          },
          {
            key: 'X-Frame-Options',
            value: 'SAMEORIGIN',
          },
          {
            key: 'X-Content-Type-Options',
            value: 'nosniff',
          },
          {
            key: 'Referrer-Policy',
            value: 'origin-when-cross-origin',
          },
        ],
      },
    ];
  },
  
  // Redirects
  async redirects() {
    return [
      {
        source: '/home',
        destination: '/',
        permanent: true,
      },
    ];
  },
};

export default nextConfig;
Checklist:

 Typed routes enabled
 Server actions configured
 Image domains whitelisted
 Security headers applied
 Environment variables exposed
File: /frontend/tsconfig.json
Purpose: TypeScript configuration

Contents:

JSON

{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"],
      "@/components/*": ["./src/components/*"],
      "@/lib/*": ["./src/lib/*"],
      "@/hooks/*": ["./src/hooks/*"],
      "@/styles/*": ["./src/styles/*"],
      "@/types/*": ["./src/types/*"],
      "@/stores/*": ["./src/stores/*"],
      "@/api/*": ["./src/api/*"]
    },
    "noUncheckedIndexedAccess": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true
  },
  "include": [
    "next-env.d.ts",
    "**/*.ts",
    "**/*.tsx",
    ".next/types/**/*.ts"
  ],
  "exclude": ["node_modules"]
}
Checklist:

 Strict mode enabled
 Path aliases configured
 No unchecked indexed access
 Unused variable detection
Phase 0 Completion Checklist
 Root directory structure created
 Docker Compose file with all services
 Makefile with developer shortcuts
 PostgreSQL initialization script
 Backend Dockerfile and dependencies
 Frontend Dockerfile and dependencies
 Environment variable templates
 TypeScript strict configuration
 Git hooks configured (optional: husky)
 README.md with setup instructions
═══════════════════════════════════════════════════════════════════════════════
PHASE 1: DESIGN SYSTEM & TOKEN ARCHITECTURE
═══════════════════════════════════════════════════════════════════════════════
OBJECTIVE: Extract design tokens from the static HTML mockup and establish
a comprehensive design system using Tailwind CSS v4's CSS-first configuration.
ESTIMATED EFFORT: 6-8 hours
DEPENDENCIES: Phase 0 completed
BLOCKERS FOR: Phase 3 (Frontend Foundation)
DESIGN AUTHORITY: The static HTML mockup is the ONLY source of truth.
All tokens, colors, typography, and spacing MUST be extracted from it.
═══════════════════════════════════════════════════════════════════════════════
Phase 1.1: CSS Custom Properties & Tailwind Configuration
File: /frontend/src/styles/tokens.css
Purpose: Design token definitions using CSS custom properties (native cascade layers)

Token Categories to Extract:

CSS

/* ═══════════════════════════════════════════════════════════════
   MORNING BREW COLLECTIVE — DESIGN TOKENS
   Source: Static HTML Mockup (Authoritative)
   ═══════════════════════════════════════════════════════════════ */

@layer tokens {
  :root {
    /* ─────────────────────────────────────────────────────────────
       COLOR SYSTEM — "SUNRISE AT THE KOPITIAM"
       ───────────────────────────────────────────────────────────── */
    
    /* Primary Palette — Cheerful Morning Warmth */
    --color-sunrise-coral: 255 107 74;           /* #FF6B4A */
    --color-sunrise-coral-light: 255 138 112;    /* #FF8A70 */
    --color-sunrise-coral-dark: 229 90 58;       /* #E55A3A */
    
    --color-golden-hour: 255 190 79;             /* #FFBE4F */
    --color-golden-hour-light: 255 208 128;      /* #FFD080 */
    --color-golden-hour-dark: 229 160 48;        /* #E5A030 */
    
    /* Coffee Essence — Supporting Browns */
    --color-espresso-dark: 61 35 23;             /* #3D2317 */
    --color-coffee-medium: 107 68 35;            /* #6B4423 */
    --color-coffee-light: 139 99 68;             /* #8B6344 */
    --color-mocha-cream: 196 164 132;            /* #C4A484 */
    
    /* Surfaces — Backgrounds & Cards */
    --color-latte-cream: 255 245 230;            /* #FFF5E6 */
    --color-latte-cream-warm: 255 240 217;       /* #FFF0D9 */
    --color-ceramic-white: 253 252 249;          /* #FDFCF9 */
    --color-paper-aged: 249 243 232;             /* #F9F3E8 */
    
    /* Accent — Refreshing Mint */
    --color-mint-fresh: 184 230 212;             /* #B8E6D4 */
    --color-mint-deep: 126 205 176;              /* #7ECDB0 */
    --color-teal-retro: 78 205 196;              /* #4ECDC4 */
    
    /* Semantic */
    --color-success: 124 179 66;                 /* #7CB342 */
    --color-error: 229 57 53;                    /* #E53935 */
    --color-warning: 255 193 7;                  /* #FFC107 */
    --color-info: 78 205 196;                    /* #4ECDC4 */
    
    /* Decorative */
    --color-tile-pattern-1: 255 228 204;         /* #FFE4CC */
    --color-tile-pattern-2: 255 212 184;         /* #FFD4B8 */
    
    /* ─────────────────────────────────────────────────────────────
       TYPOGRAPHY SYSTEM
       ───────────────────────────────────────────────────────────── */
    
    /* Font Families */
    --font-display: 'Righteous', cursive;
    --font-body: 'Nunito', -apple-system, BlinkMacSystemFont, sans-serif;
    --font-mono: 'JetBrains Mono', monospace;
    
    /* Font Sizes — Fluid Scale */
    --text-xs: clamp(0.75rem, 0.7rem + 0.25vw, 0.8125rem);
    --text-sm: clamp(0.8125rem, 0.77rem + 0.21vw, 0.9375rem);
    --text-base: clamp(0.9375rem, 0.89rem + 0.25vw, 1.0625rem);
    --text-lg: clamp(1.0625rem, 1rem + 0.31vw, 1.25rem);
    --text-xl: clamp(1.25rem, 1.16rem + 0.45vw, 1.5rem);
    --text-2xl: clamp(1.5rem, 1.36rem + 0.71vw, 1.875rem);
    --text-3xl: clamp(1.875rem, 1.65rem + 1.12vw, 2.5rem);
    --text-4xl: clamp(2.5rem, 2.1rem + 2vw, 3.5rem);
    --text-5xl: clamp(3rem, 2.5rem + 2.5vw, 4.5rem);
    
    /* Line Heights */
    --leading-none: 1;
    --leading-tight: 1.1;
    --leading-snug: 1.35;
    --leading-normal: 1.6;
    --leading-relaxed: 1.7;
    --leading-loose: 1.8;
    
    /* Letter Spacing */
    --tracking-tighter: -0.03em;
    --tracking-tight: -0.01em;
    --tracking-normal: 0;
    --tracking-wide: 0.02em;
    --tracking-wider: 0.05em;
    --tracking-widest: 0.15em;
    
    /* ─────────────────────────────────────────────────────────────
       SPACING SYSTEM — 8pt Grid
       ───────────────────────────────────────────────────────────── */
    
    --space-0: 0;
    --space-px: 1px;
    --space-0-5: 0.125rem;   /* 2px */
    --space-1: 0.25rem;      /* 4px */
    --space-2: 0.5rem;       /* 8px */
    --space-3: 0.75rem;      /* 12px */
    --space-4: 1rem;         /* 16px */
    --space-5: 1.25rem;      /* 20px */
    --space-6: 1.5rem;       /* 24px */
    --space-8: 2rem;         /* 32px */
    --space-10: 2.5rem;      /* 40px */
    --space-12: 3rem;        /* 48px */
    --space-16: 4rem;        /* 64px */
    --space-20: 5rem;        /* 80px */
    --space-24: 6rem;        /* 96px */
    --space-32: 8rem;        /* 128px */
    
    /* ─────────────────────────────────────────────────────────────
       BORDER RADIUS — Soft & Rounded (70s Aesthetic)
       ───────────────────────────────────────────────────────────── */
    
    --radius-none: 0;
    --radius-sm: 8px;
    --radius-md: 16px;
    --radius-lg: 24px;
    --radius-xl: 32px;
    --radius-2xl: 48px;
    --radius-full: 9999px;
    
    /* ─────────────────────────────────────────────────────────────
       SHADOWS — Warm & Inviting
       ───────────────────────────────────────────────────────────── */
    
    --shadow-color: 107 68 35;
    --shadow-warm: 0 2px 8px rgb(var(--shadow-color) / 0.15);
    --shadow-md: 0 4px 16px rgb(var(--shadow-color) / 0.15);
    --shadow-lg: 0 8px 32px rgb(var(--shadow-color) / 0.15);
    --shadow-xl: 0 16px 48px rgb(var(--shadow-color) / 0.2);
    --shadow-glow-coral: 0 0 40px rgb(var(--color-sunrise-coral) / 0.2);
    --shadow-button: 0 4px 0 rgb(var(--color-sunrise-coral-dark) / 1);
    
    /* ─────────────────────────────────────────────────────────────
       ANIMATION — Motion Tokens
       ───────────────────────────────────────────────────────────── */
    
    --ease-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);
    --ease-smooth: cubic-bezier(0.23, 1, 0.32, 1);
    --ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
    
    --duration-instant: 0ms;
    --duration-fast: 150ms;
    --duration-normal: 300ms;
    --duration-slow: 500ms;
    --duration-slower: 700ms;
    
    /* ─────────────────────────────────────────────────────────────
       Z-INDEX SCALE
       ───────────────────────────────────────────────────────────── */
    
    --z-base: 0;
    --z-dropdown: 100;
    --z-sticky: 200;
    --z-overlay: 300;
    --z-modal: 400;
    --z-toast: 500;
    
    /* ─────────────────────────────────────────────────────────────
       LAYOUT TOKENS
       ───────────────────────────────────────────────────────────── */
    
    --container-max: 1200px;
    --container-padding: var(--space-6);
    --nav-height: 72px;
    --section-padding: var(--space-24);
  }
  
  /* ─────────────────────────────────────────────────────────────
     DARK MODE OVERRIDES (Future Enhancement)
     ───────────────────────────────────────────────────────────── */
  
  @media (prefers-color-scheme: dark) {
    :root {
      /* Dark mode tokens to be defined */
    }
  }
}
Checklist:

 All colors extracted from static HTML
 Colors defined as RGB space-separated values (for Tailwind opacity)
 Typography scale with fluid clamp values
 8pt grid spacing system
 Soft rounded border radius matching 70s aesthetic
 Warm brown-tinted shadows
 Animation easings with bounce effect
 Z-index scale for layering
File: /frontend/src/styles/globals.css
Purpose: Global styles, base resets, and Tailwind integration

Contents:

CSS

/* ═══════════════════════════════════════════════════════════════
   MORNING BREW COLLECTIVE — GLOBAL STYLES
   ═══════════════════════════════════════════════════════════════ */

@import "tailwindcss";
@import "./tokens.css";

/* ─────────────────────────────────────────────────────────────
   CSS LAYERS — Cascade Control
   ───────────────────────────────────────────────────────────── */

@layer base {
  /* Reset & Normalization */
  *, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  html {
    scroll-behavior: smooth;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-size-adjust: 100%;
    tab-size: 4;
  }

  body {
    font-family: var(--font-body);
    font-size: var(--text-base);
    line-height: var(--leading-normal);
    color: rgb(var(--color-espresso-dark));
    background-color: rgb(var(--color-latte-cream));
    overflow-x: hidden;
  }

  /* Typography Defaults */
  h1, h2, h3, h4, h5, h6 {
    font-family: var(--font-display);
    line-height: var(--leading-tight);
    color: rgb(var(--color-espresso-dark));
  }

  h1 { font-size: var(--text-5xl); }
  h2 { font-size: var(--text-4xl); }
  h3 { font-size: var(--text-3xl); }
  h4 { font-size: var(--text-2xl); }
  h5 { font-size: var(--text-xl); }
  h6 { font-size: var(--text-lg); }

  p {
    margin-bottom: var(--space-4);
  }

  a {
    color: inherit;
    text-decoration: none;
    transition: color var(--duration-normal) var(--ease-smooth);
  }

  img, svg, video, canvas {
    display: block;
    max-width: 100%;
    height: auto;
  }

  button {
    font-family: inherit;
    cursor: pointer;
    border: none;
    background: none;
  }

  ul, ol {
    list-style: none;
  }

  /* Focus Visible — Accessibility */
  :focus-visible {
    outline: 3px solid rgb(var(--color-sunrise-coral));
    outline-offset: 3px;
  }

  /* Selection */
  ::selection {
    background-color: rgb(var(--color-golden-hour));
    color: rgb(var(--color-espresso-dark));
  }
}

@layer components {
  /* Container */
  .container {
    width: 100%;
    max-width: var(--container-max);
    margin-inline: auto;
    padding-inline: var(--container-padding);
  }

  /* Skip Link — Accessibility */
  .skip-link {
    position: absolute;
    top: -100%;
    left: var(--space-4);
    background: rgb(var(--color-espresso-dark));
    color: rgb(var(--color-ceramic-white));
    padding: var(--space-3) var(--space-6);
    border-radius: var(--radius-md);
    font-weight: 700;
    z-index: var(--z-toast);
    transition: top var(--duration-normal) var(--ease-smooth);
  }

  .skip-link:focus {
    top: var(--space-4);
  }

  /* Screen Reader Only */
  .sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border: 0;
  }
}

@layer utilities {
  /* Animation Utilities */
  .animate-float {
    animation: float 3s ease-in-out infinite;
  }

  @keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-8px); }
  }

  .animate-pulse-glow {
    animation: pulse-glow 4s ease-in-out infinite;
  }

  @keyframes pulse-glow {
    0%, 100% { transform: scale(1); opacity: 0.6; }
    50% { transform: scale(1.1); opacity: 0.4; }
  }

  .animate-steam {
    animation: steam-rise 2s ease-in-out infinite;
  }

  @keyframes steam-rise {
    0%, 100% { opacity: 0; transform: translateY(0) scaleY(0.5); }
    50% { opacity: 1; transform: translateY(-20px) scaleY(1); }
  }

  /* Sunburst Background */
  .bg-sunburst {
    position: relative;
    overflow: hidden;
  }

  .bg-sunburst::before {
    content: '';
    position: absolute;
    inset: 0;
    background: repeating-conic-gradient(
      from 0deg,
      rgb(var(--color-golden-hour)) 0deg 10deg,
      rgb(var(--color-latte-cream-warm)) 10deg 20deg
    );
    opacity: 0.15;
    animation: sunburst-rotate 120s linear infinite;
    pointer-events: none;
  }

  @keyframes sunburst-rotate {
    to { transform: rotate(360deg); }
  }
}

/* ─────────────────────────────────────────────────────────────
   REDUCED MOTION — Accessibility
   ───────────────────────────────────────────────────────────── */

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}

/* ─────────────────────────────────────────────────────────────
   PRINT STYLES
   ───────────────────────────────────────────────────────────── */

@media print {
  .no-print {
    display: none !important;
  }

  body {
    background: white;
    color: black;
  }
}
Checklist:

 Tailwind CSS v4 imported
 Token file imported
 CSS layers defined (base, components, utilities)
 Reset styles applied
 Typography defaults configured
 Focus visible styles for accessibility
 Custom animation utilities
 Reduced motion media query
 Print styles
File: /frontend/tailwind.config.ts
Purpose: Tailwind CSS v4 configuration extending tokens

Contents:

TypeScript

import type { Config } from 'tailwindcss';

const config: Config = {
  content: [
    './src/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        // Primary Palette
        coral: {
          DEFAULT: 'rgb(var(--color-sunrise-coral) / <alpha-value>)',
          light: 'rgb(var(--color-sunrise-coral-light) / <alpha-value>)',
          dark: 'rgb(var(--color-sunrise-coral-dark) / <alpha-value>)',
        },
        golden: {
          DEFAULT: 'rgb(var(--color-golden-hour) / <alpha-value>)',
          light: 'rgb(var(--color-golden-hour-light) / <alpha-value>)',
          dark: 'rgb(var(--color-golden-hour-dark) / <alpha-value>)',
        },
        // Coffee Browns
        espresso: 'rgb(var(--color-espresso-dark) / <alpha-value>)',
        coffee: {
          DEFAULT: 'rgb(var(--color-coffee-medium) / <alpha-value>)',
          light: 'rgb(var(--color-coffee-light) / <alpha-value>)',
        },
        mocha: 'rgb(var(--color-mocha-cream) / <alpha-value>)',
        // Surfaces
        latte: {
          DEFAULT: 'rgb(var(--color-latte-cream) / <alpha-value>)',
          warm: 'rgb(var(--color-latte-cream-warm) / <alpha-value>)',
        },
        ceramic: 'rgb(var(--color-ceramic-white) / <alpha-value>)',
        paper: 'rgb(var(--color-paper-aged) / <alpha-value>)',
        // Accent
        mint: {
          DEFAULT: 'rgb(var(--color-mint-fresh) / <alpha-value>)',
          deep: 'rgb(var(--color-mint-deep) / <alpha-value>)',
        },
        teal: 'rgb(var(--color-teal-retro) / <alpha-value>)',
        // Semantic
        success: 'rgb(var(--color-success) / <alpha-value>)',
        error: 'rgb(var(--color-error) / <alpha-value>)',
        warning: 'rgb(var(--color-warning) / <alpha-value>)',
        info: 'rgb(var(--color-info) / <alpha-value>)',
        // Decorative
        tile: {
          1: 'rgb(var(--color-tile-pattern-1) / <alpha-value>)',
          2: 'rgb(var(--color-tile-pattern-2) / <alpha-value>)',
        },
      },
      fontFamily: {
        display: ['var(--font-display)'],
        body: ['var(--font-body)'],
        mono: ['var(--font-mono)'],
      },
      fontSize: {
        xs: 'var(--text-xs)',
        sm: 'var(--text-sm)',
        base: 'var(--text-base)',
        lg: 'var(--text-lg)',
        xl: 'var(--text-xl)',
        '2xl': 'var(--text-2xl)',
        '3xl': 'var(--text-3xl)',
        '4xl': 'var(--text-4xl)',
        '5xl': 'var(--text-5xl)',
      },
      spacing: {
        '0.5': 'var(--space-0-5)',
        '1': 'var(--space-1)',
        '2': 'var(--space-2)',
        '3': 'var(--space-3)',
        '4': 'var(--space-4)',
        '5': 'var(--space-5)',
        '6': 'var(--space-6)',
        '8': 'var(--space-8)',
        '10': 'var(--space-10)',
        '12': 'var(--space-12)',
        '16': 'var(--space-16)',
        '20': 'var(--space-20)',
        '24': 'var(--space-24)',
        '32': 'var(--space-32)',
      },
      borderRadius: {
        none: 'var(--radius-none)',
        sm: 'var(--radius-sm)',
        DEFAULT: 'var(--radius-md)',
        md: 'var(--radius-md)',
        lg: 'var(--radius-lg)',
        xl: 'var(--radius-xl)',
        '2xl': 'var(--radius-2xl)',
        full: 'var(--radius-full)',
      },
      boxShadow: {
        warm: 'var(--shadow-warm)',
        DEFAULT: 'var(--shadow-md)',
        md: 'var(--shadow-md)',
        lg: 'var(--shadow-lg)',
        xl: 'var(--shadow-xl)',
        glow: 'var(--shadow-glow-coral)',
        button: 'var(--shadow-button)',
      },
      transitionTimingFunction: {
        bounce: 'var(--ease-bounce)',
        smooth: 'var(--ease-smooth)',
      },
      transitionDuration: {
        fast: 'var(--duration-fast)',
        normal: 'var(--duration-normal)',
        slow: 'var(--duration-slow)',
      },
      zIndex: {
        dropdown: 'var(--z-dropdown)',
        sticky: 'var(--z-sticky)',
        overlay: 'var(--z-overlay)',
        modal: 'var(--z-modal)',
        toast: 'var(--z-toast)',
      },
      height: {
        nav: 'var(--nav-height)',
      },
      maxWidth: {
        container: 'var(--container-max)',
      },
    },
  },
  plugins: [],
};

export default config;
Checklist:

 All color tokens mapped to Tailwind classes
 Alpha value support for opacity utilities
 Custom font families registered
 Fluid typography scale integrated
 8pt spacing system mapped
 Rounded radius scale configured
 Warm shadow utilities
 Custom animation easings
 Z-index scale
Phase 1.2: Utility Functions & Helpers
File: /frontend/src/lib/utils.ts
Purpose: Utility functions for class merging and styling

Contents:

TypeScript

import { type ClassValue, clsx } from 'clsx';
import { twMerge } from 'tailwind-merge';

/**
 * Merges class names with Tailwind conflict resolution
 * Uses clsx for conditional classes and tailwind-merge for deduplication
 */
export function cn(...inputs: ClassValue[]): string {
  return twMerge(clsx(inputs));
}

/**
 * Format price in Singapore Dollars
 * @param amount - Price in cents or dollars
 * @param options - Formatting options
 */
export function formatPrice(
  amount: number,
  options: {
    currency?: string;
    inCents?: boolean;
  } = {}
): string {
  const { currency = 'SGD', inCents = false } = options;
  const value = inCents ? amount / 100 : amount;

  return new Intl.NumberFormat('en-SG', {
    style: 'currency',
    currency,
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  }).format(value);
}

/**
 * Calculate GST from price (Singapore 9%)
 * @param price - Price in dollars (inclusive of GST)
 */
export function calculateGST(price: number): {
  subtotal: number;
  gst: number;
  total: number;
} {
  const GST_RATE = 0.09;
  const subtotal = price / (1 + GST_RATE);
  const gst = price - subtotal;

  return {
    subtotal: Math.round(subtotal * 100) / 100,
    gst: Math.round(gst * 100) / 100,
    total: price,
  };
}

/**
 * Slugify a string for URLs
 */
export function slugify(text: string): string {
  return text
    .toLowerCase()
    .trim()
    .replace(/[^\w\s-]/g, '')
    .replace(/[\s_-]+/g, '-')
    .replace(/^-+|-+$/g, '');
}

/**
 * Truncate text with ellipsis
 */
export function truncate(text: string, length: number): string {
  if (text.length <= length) return text;
  return text.slice(0, length).trim() + '...';
}

/**
 * Generate unique ID
 */
export function generateId(prefix = 'id'): string {
  return `${prefix}-${Math.random().toString(36).substr(2, 9)}`;
}

/**
 * Delay utility for animations
 */
export function delay(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

/**
 * Check if code is running on server
 */
export const isServer = typeof window === 'undefined';

/**
 * Check if code is running on client
 */
export const isClient = !isServer;
Checklist:

 cn() function for Tailwind class merging
 Singapore currency formatting
 GST calculation (9% inclusive)
 String utilities (slugify, truncate)
 ID generation
 Environment detection
Phase 1.3: Typography Component
File: /frontend/src/components/ui/typography.tsx
Purpose: Semantic typography components with design system integration

Contents:

TypeScript

import * as React from 'react';
import { cva, type VariantProps } from 'class-variance-authority';
import { cn } from '@/lib/utils';

/* ═══════════════════════════════════════════════════════════════
   HEADING COMPONENTS
   ═══════════════════════════════════════════════════════════════ */

const headingVariants = cva('font-display text-espresso', {
  variants: {
    level: {
      h1: 'text-5xl leading-tight tracking-tight',
      h2: 'text-4xl leading-tight',
      h3: 'text-3xl leading-snug',
      h4: 'text-2xl leading-snug',
      h5: 'text-xl leading-normal',
      h6: 'text-lg leading-normal',
    },
  },
  defaultVariants: {
    level: 'h2',
  },
});

interface HeadingProps
  extends React.HTMLAttributes<HTMLHeadingElement>,
    VariantProps<typeof headingVariants> {
  as?: 'h1' | 'h2' | 'h3' | 'h4' | 'h5' | 'h6';
}

export function Heading({
  as,
  level,
  className,
  children,
  ...props
}: HeadingProps) {
  const Component = as || level || 'h2';
  const appliedLevel = level || as || 'h2';

  return (
    <Component
      className={cn(headingVariants({ level: appliedLevel }), className)}
      {...props}
    >
      {children}
    </Component>
  );
}

/* ═══════════════════════════════════════════════════════════════
   TEXT COMPONENTS
   ═══════════════════════════════════════════════════════════════ */

const textVariants = cva('font-body', {
  variants: {
    size: {
      xs: 'text-xs',
      sm: 'text-sm',
      base: 'text-base',
      lg: 'text-lg',
      xl: 'text-xl',
    },
    weight: {
      normal: 'font-normal',
      medium: 'font-medium',
      semibold: 'font-semibold',
      bold: 'font-bold',
      extrabold: 'font-extrabold',
    },
    color: {
      default: 'text-espresso',
      muted: 'text-coffee',
      light: 'text-coffee-light',
      coral: 'text-coral',
      golden: 'text-golden',
      white: 'text-white',
    },
    leading: {
      none: 'leading-none',
      tight: 'leading-tight',
      snug: 'leading-snug',
      normal: 'leading-normal',
      relaxed: 'leading-relaxed',
      loose: 'leading-loose',
    },
  },
  defaultVariants: {
    size: 'base',
    weight: 'normal',
    color: 'default',
    leading: 'normal',
  },
});

interface TextProps
  extends React.HTMLAttributes<HTMLParagraphElement>,
    VariantProps<typeof textVariants> {
  as?: 'p' | 'span' | 'div' | 'label';
}

export function Text({
  as: Component = 'p',
  size,
  weight,
  color,
  leading,
  className,
  children,
  ...props
}: TextProps) {
  return (
    <Component
      className={cn(textVariants({ size, weight, color, leading }), className)}
      {...props}
    >
      {children}
    </Component>
  );
}

/* ═══════════════════════════════════════════════════════════════
   DISPLAY TEXT — Hero Titles
   ═══════════════════════════════════════════════════════════════ */

interface DisplayProps extends React.HTMLAttributes<HTMLSpanElement> {
  highlight?: boolean;
}

export function Display({ highlight, className, children, ...props }: DisplayProps) {
  return (
    <span
      className={cn(
        'font-display text-5xl leading-tight text-espresso',
        highlight && 'block text-coral relative',
        className
      )}
      {...props}
    >
      {children}
      {highlight && (
        <span
          className="absolute bottom-0 left-0 right-0 h-2 bg-golden rounded-full -z-10 scale-x-90"
          aria-hidden="true"
        />
      )}
    </span>
  );
}

/* ═══════════════════════════════════════════════════════════════
   DROP CAP — Editorial Style
   ═══════════════════════════════════════════════════════════════ */

interface DropCapProps extends React.HTMLAttributes<HTMLSpanElement> {
  letter: string;
}

export function DropCap({ letter, className, ...props }: DropCapProps) {
  return (
    <span
      className={cn(
        'float-left font-display text-[5rem] leading-[0.8] mr-4 mt-2 text-coral',
        'drop-shadow-[3px_3px_0_rgb(var(--color-ceramic-white))]',
        className
      )}
      aria-hidden="true"
      {...props}
    >
      {letter}
    </span>
  );
}

/* ═══════════════════════════════════════════════════════════════
   LABEL — Form Labels
   ═══════════════════════════════════════════════════════════════ */

export function Label({
  className,
  children,
  ...props
}: React.LabelHTMLAttributes<HTMLLabelElement>) {
  return (
    <label
      className={cn(
        'text-sm font-semibold text-espresso leading-none',
        'peer-disabled:cursor-not-allowed peer-disabled:opacity-70',
        className
      )}
      {...props}
    >
      {children}
    </label>
  );
}
Checklist:

 Heading component with semantic levels
 Text component with size/weight/color variants
 Display component for hero titles with highlight effect
 DropCap for editorial style paragraphs
 Label component for forms
 All using CVA for variant management
 Tailwind classes from design tokens
Phase 1 Completion Checklist
 Design tokens extracted to CSS custom properties
 Tailwind CSS v4 configuration complete
 Global styles with base resets
 Utility functions library
 Typography components
 Animation keyframes defined
 Reduced motion support
 Print styles
═══════════════════════════════════════════════════════════════════════════════
PHASE 2: BACKEND DOMAIN CORE (LARAVEL)
═══════════════════════════════════════════════════════════════════════════════
OBJECTIVE: Establish the Laravel backend with domain models, database schema,
API structure, and core business logic for the e-commerce platform.
ESTIMATED EFFORT: 16-24 hours
DEPENDENCIES: Phase 0 completed
BLOCKERS FOR: Phase 4 (E-commerce Engine), Phase 5 (Compliance)
ARCHITECTURAL PRINCIPLE: Domain-Driven Design with clear bounded contexts
═══════════════════════════════════════════════════════════════════════════════
Phase 2.1: Database Schema Design
File: /backend/database/migrations/2024_01_01_000001_create_products_table.php
Purpose: Products/Menu items storage

Schema:

PHP

<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('products', function (Blueprint $table) {
            $table->uuid('id')->primary();
            $table->string('name');
            $table->string('slug')->unique();
            $table->text('description')->nullable();
            $table->text('short_description')->nullable();
            
            // Pricing (stored in cents, SGD)
            $table->integer('price_cents');
            $table->integer('compare_at_price_cents')->nullable();
            
            // Categorization
            $table->string('category'); // coffee, tea, food
            $table->json('tags')->nullable(); // ['Best Seller', 'Spicy']
            
            // Inventory
            $table->integer('stock_quantity')->default(0);
            $table->boolean('track_inventory')->default(true);
            $table->boolean('allow_backorder')->default(false);
            
            // Media
            $table->string('featured_image')->nullable();
            $table->json('gallery_images')->nullable();
            $table->string('icon_emoji')->nullable(); // ☕, 🫖, 🍞
            
            // Status
            $table->enum('status', ['draft', 'active', 'archived'])->default('draft');
            $table->boolean('is_featured')->default(false);
            $table->integer('sort_order')->default(0);
            
            // Availability
            $table->json('available_at_locations')->nullable(); // Location UUIDs
            $table->time('available_from')->nullable();
            $table->time('available_until')->nullable();
            
            // SEO
            $table->string('meta_title')->nullable();
            $table->text('meta_description')->nullable();
            
            $table->timestamps();
            $table->softDeletes();
            
            // Indexes
            $table->index('category');
            $table->index('status');
            $table->index(['status', 'is_featured']);
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('products');
    }
};
Checklist:

 UUID primary key
 Price in cents (integer) for precision
 GST-inclusive pricing support
 Category and tags for filtering
 Inventory tracking fields
 Multi-location availability
 Time-based availability (breakfast items)
 SEO fields
 Soft deletes
File: /backend/database/migrations/2024_01_01_000002_create_locations_table.php
Purpose: Physical store locations

Schema:

PHP

<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('locations', function (Blueprint $table) {
            $table->uuid('id')->primary();
            $table->string('name');
            $table->string('slug')->unique();
            $table->string('badge')->nullable(); // 'Flagship', 'Peranakan', 'Modern'
            
            // Address
            $table->string('address_line_1');
            $table->string('address_line_2')->nullable();
            $table->string('postal_code', 6);
            $table->string('city')->default('Singapore');
            $table->string('country_code', 2)->default('SG');
            
            // Geolocation
            $table->decimal('latitude', 10, 8)->nullable();
            $table->decimal('longitude', 11, 8)->nullable();
            
            // Contact
            $table->string('phone')->nullable();
            $table->string('email')->nullable();
            
            // Operating Hours (JSON for flexibility)
            $table->json('operating_hours')->nullable();
            /*
              {
                "monday": { "open": "07:00", "close": "20:00" },
                "tuesday": { "open": "07:00", "close": "20:00" },
                ...
              }
            */
            
            // Features
            $table->json('features')->nullable(); // ['Full Breakfast', 'Accessible', 'Parking']
            
            // Media
            $table->string('featured_image')->nullable();
            $table->json('gallery_images')->nullable();
            $table->string('icon_emoji')->nullable();
            
            // Status
            $table->boolean('is_active')->default(true);
            $table->boolean('accepts_online_orders')->default(true);
            $table->boolean('accepts_reservations')->default(false);
            $table->integer('sort_order')->default(0);
            
            $table->timestamps();
            $table->softDeletes();
            
            $table->index('is_active');
            $table->index('postal_code');
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('locations');
    }
};
Checklist:

 Singapore postal code format (6 digits)
 Geolocation for map integration
 Flexible operating hours JSON
 Feature flags for amenities
 Online order and reservation toggles
File: /backend/database/migrations/2024_01_01_000003_create_customers_table.php
Purpose: Customer accounts (extends Laravel users)

Schema:

PHP

<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('customers', function (Blueprint $table) {
            $table->uuid('id')->primary();
            
            // Authentication
            $table->string('email')->unique();
            $table->timestamp('email_verified_at')->nullable();
            $table->string('password')->nullable(); // Nullable for guest checkout
            $table->string('phone')->nullable();
            $table->boolean('phone_verified')->default(false);
            
            // Profile
            $table->string('first_name')->nullable();
            $table->string('last_name')->nullable();
            $table->date('date_of_birth')->nullable();
            
            // PDPA Compliance
            $table->boolean('marketing_consent')->default(false);
            $table->timestamp('marketing_consent_at')->nullable();
            $table->string('pdpa_consent_version')->nullable();
            
            // Preferences
            $table->uuid('default_location_id')->nullable();
            $table->string('preferred_language', 5)->default('en');
            
            // Loyalty (future)
            $table->integer('loyalty_points')->default(0);
            $table->string('loyalty_tier')->default('bronze');
            
            // Status
            $table->boolean('is_active')->default(true);
            $table->timestamp('last_login_at')->nullable();
            $table->string('last_login_ip')->nullable();
            
            $table->rememberToken();
            $table->timestamps();
            $table->softDeletes();
            
            $table->index('email');
            $table->index('phone');
            
            $table->foreign('default_location_id')
                  ->references('id')
                  ->on('locations')
                  ->nullOnDelete();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('customers');
    }
};
Checklist:

 Separate from admin users
 Guest checkout support (nullable password)
 PDPA consent tracking with version
 Marketing opt-in with timestamp
 Loyalty program fields
 Preferred location relationship
File: /backend/database/migrations/2024_01_01_000004_create_orders_table.php
Purpose: Order records with Singapore compliance

Schema:

PHP

<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('orders', function (Blueprint $table) {
            $table->uuid('id')->primary();
            $table->string('order_number')->unique(); // MBC-2024-000001
            
            // Customer
            $table->uuid('customer_id')->nullable();
            $table->string('customer_email');
            $table->string('customer_phone')->nullable();
            $table->string('customer_name');
            
            // Fulfillment
            $table->uuid('location_id');
            $table->enum('fulfillment_type', ['pickup', 'dine_in', 'delivery'])->default('pickup');
            $table->timestamp('scheduled_at')->nullable();
            $table->text('special_instructions')->nullable();
            
            // Pricing (all in cents, SGD)
            $table->integer('subtotal_cents'); // Before GST
            $table->integer('gst_cents'); // 9% GST
            $table->integer('discount_cents')->default(0);
            $table->integer('delivery_fee_cents')->default(0);
            $table->integer('total_cents'); // Final amount
            
            // GST Breakdown for InvoiceNow
            $table->decimal('gst_rate', 5, 4)->default(0.0900); // 9%
            $table->string('gst_registration_number')->nullable();
            
            // Payment
            $table->enum('payment_status', [
                'pending',
                'authorized',
                'paid',
                'partially_refunded',
                'refunded',
                'failed'
            ])->default('pending');
            $table->string('payment_method')->nullable(); // stripe, paynow
            $table->string('payment_intent_id')->nullable();
            $table->timestamp('paid_at')->nullable();
            
            // Order Status
            $table->enum('status', [
                'pending',
                'confirmed',
                'preparing',
                'ready',
                'completed',
                'cancelled'
            ])->default('pending');
            $table->timestamp('confirmed_at')->nullable();
            $table->timestamp('preparing_at')->nullable();
            $table->timestamp('ready_at')->nullable();
            $table->timestamp('completed_at')->nullable();
            $table->timestamp('cancelled_at')->nullable();
            $table->text('cancellation_reason')->nullable();
            
            // InvoiceNow (PEPPOL)
            $table->boolean('invoice_now_required')->default(false);
            $table->string('invoice_now_id')->nullable();
            $table->timestamp('invoice_now_sent_at')->nullable();
            
            // Metadata
            $table->json('metadata')->nullable();
            $table->string('source')->default('web'); // web, app, pos
            $table->string('ip_address')->nullable();
            $table->string('user_agent')->nullable();
            
            $table->timestamps();
            $table->softDeletes();
            
            // Indexes
            $table->index('order_number');
            $table->index('customer_id');
            $table->index('status');
            $table->index('payment_status');
            $table->index(['status', 'location_id']);
            $table->index('created_at');
            
            $table->foreign('customer_id')
                  ->references('id')
                  ->on('customers')
                  ->nullOnDelete();
                  
            $table->foreign('location_id')
                  ->references('id')
                  ->on('locations');
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('orders');
    }
};
Checklist:

 Sequential order number generation
 Singapore GST calculation fields
 InvoiceNow/PEPPOL support fields
 Multiple fulfillment types
 Comprehensive status tracking with timestamps
 Payment status separate from order status
 Audit fields (IP, user agent, source)
File: /backend/database/migrations/2024_01_01_000005_create_order_items_table.php
Purpose: Order line items

Schema:

PHP

<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('order_items', function (Blueprint $table) {
            $table->uuid('id')->primary();
            $table->uuid('order_id');
            $table->uuid('product_id');
            
            // Snapshot at time of order (products may change)
            $table->string('product_name');
            $table->string('product_sku')->nullable();
            
            // Quantity & Pricing
            $table->integer('quantity');
            $table->integer('unit_price_cents'); // Price per item
            $table->integer('total_cents'); // quantity * unit_price
            
            // Customizations
            $table->json('options')->nullable();
            /*
              {
                "sugar_level": "less",
                "ice": "no_ice",
                "size": "large"
              }
            */
            
            $table->text('notes')->nullable();
            
            $table->timestamps();
            
            $table->foreign('order_id')
                  ->references('id')
                  ->on('orders')
                  ->cascadeOnDelete();
                  
            $table->foreign('product_id')
                  ->references('id')
                  ->on('products');
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('order_items');
    }
};
Checklist:

 Product snapshot (name preserved)
 Customization options (drink modifications)
 Line item totals
File: /backend/database/migrations/2024_01_01_000006_create_inventory_reservations_table.php
Purpose: Two-phase inventory reservation system

Schema:

PHP

<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('inventory_reservations', function (Blueprint $table) {
            $table->uuid('id')->primary();
            $table->uuid('product_id');
            $table->uuid('location_id');
            $table->uuid('order_id')->nullable();
            $table->string('session_id')->nullable();
            
            $table->integer('quantity');
            
            $table->enum('status', [
                'pending',    // In cart, not committed
                'committed',  // Order placed
                'released',   // Returned to inventory
                'consumed'    // Order completed
            ])->default('pending');
            
            $table->timestamp('expires_at');
            $table->timestamp('committed_at')->nullable();
            $table->timestamp('released_at')->nullable();
            
            $table->timestamps();
            
            $table->index(['product_id', 'status']);
            $table->index('expires_at');
            $table->index('session_id');
            
            $table->foreign('product_id')
                  ->references('id')
                  ->on('products');
                  
            $table->foreign('location_id')
                  ->references('id')
                  ->on('locations');
                  
            $table->foreign('order_id')
                  ->references('id')
                  ->on('orders')
                  ->nullOnDelete();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('inventory_reservations');
    }
};
Checklist:

 Session-based pending reservations
 Order-linked committed reservations
 Expiry for abandoned cart cleanup
 Status lifecycle tracking
File: /backend/database/migrations/2024_01_01_000007_create_newsletter_subscriptions_table.php
Purpose: PDPA-compliant newsletter subscriptions

Schema:

PHP

<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('newsletter_subscriptions', function (Blueprint $table) {
            $table->uuid('id')->primary();
            $table->string('email')->unique();
            $table->uuid('customer_id')->nullable();
            
            // PDPA Compliance
            $table->string('consent_version');
            $table->text('consent_text');
            $table->timestamp('consented_at');
            $table->string('consent_ip');
            $table->string('consent_user_agent')->nullable();
            
            // Status
            $table->boolean('is_active')->default(true);
            $table->timestamp('unsubscribed_at')->nullable();
            $table->string('unsubscribe_reason')->nullable();
            
            // Verification
            $table->string('verification_token')->nullable();
            $table->timestamp('verified_at')->nullable();
            
            // Source
            $table->string('source')->default('website');
            
            $table->timestamps();
            
            $table->index('email');
            $table->index('is_active');
            
            $table->foreign('customer_id')
                  ->references('id')
                  ->on('customers')
                  ->nullOnDelete();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('newsletter_subscriptions');
    }
};
Checklist:

 Consent version tracking
 Full consent text stored
 IP address for audit
 Double opt-in verification
 Unsubscribe tracking
Phase 2.2: Eloquent Models
File: /backend/app/Models/Product.php
Purpose: Product domain model

Contents:

PHP

<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Concerns\HasUuids;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\SoftDeletes;
use Illuminate\Database\Eloquent\Relations\HasMany;
use Illuminate\Database\Eloquent\Builder;
use Spatie\Sluggable\HasSlug;
use Spatie\Sluggable\SlugOptions;

class Product extends Model
{
    use HasFactory, HasUuids, SoftDeletes, HasSlug;

    protected $fillable = [
        'name',
        'slug',
        'description',
        'short_description',
        'price_cents',
        'compare_at_price_cents',
        'category',
        'tags',
        'stock_quantity',
        'track_inventory',
        'allow_backorder',
        'featured_image',
        'gallery_images',
        'icon_emoji',
        'status',
        'is_featured',
        'sort_order',
        'available_at_locations',
        'available_from',
        'available_until',
        'meta_title',
        'meta_description',
    ];

    protected $casts = [
        'tags' => 'array',
        'gallery_images' => 'array',
        'available_at_locations' => 'array',
        'track_inventory' => 'boolean',
        'allow_backorder' => 'boolean',
        'is_featured' => 'boolean',
        'available_from' => 'datetime:H:i',
        'available_until' 
