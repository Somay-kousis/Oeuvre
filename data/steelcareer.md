# steelcareer

## Overview
Steelcareer is a structured international hiring and career coordination platform focused on human-guided recruitment instead of fully algorithmic matching.

The platform operates more like:
- a concierge hiring system
- a coordinated talent network
- a human-reviewed career ecosystem

instead of:
- a traditional job board
- automated mass-application platform

The project was designed around the belief that:
> hiring works better when trust, context, and human coordination are prioritized over pure automation.

Live Demo:
- https://steel-career-415l4p5or-somaykaush-6383s-projects.vercel.app

---

## Core Philosophy

Most hiring platforms feel:
- cold
- transactional
- algorithm-heavy
- emotionally disconnected

Steelcareer explores a different direction:
- guided introductions
- curated coordination
- human review systems
- trust-oriented hiring flows

The platform intentionally avoids:
- aggressive automation
- spam-style applications
- shallow recommendation systems

Instead, the system focuses on:
- coordination
- verification
- onboarding quality
- structured communication
- human interaction

---

## Problem Statement

Traditional hiring systems often create:
- application overload
- poor candidate visibility
- low-trust interactions
- impersonal recruitment pipelines

Steelcareer attempts to solve:
- fragmented hiring coordination
- poor onboarding experience
- recruiter-candidate disconnect
- unstructured consultation workflows

The platform serves:
- seekers
- providers
- admins

through separate role-based systems.

---

## Technical Stack

### Frontend
- Next.js 15
- TypeScript
- TailwindCSS v4
- Framer Motion

### Backend
- Supabase
- PostgreSQL
- Supabase Auth
- Row Level Security

### Forms & Validation
- React Hook Form
- Zod

### UI Systems
- shadcn/ui
- Radix UI

### Deployment
- Vercel

---

## Core Features

### Role-Based Platform Architecture
The platform supports:
- seekers
- providers
- admins

Each role has:
- dedicated onboarding
- dashboard systems
- access control
- workflow logic

---

### Seeker System
Features include:
- multi-step onboarding
- profile completion tracking
- consultation scheduling
- review status systems
- external profile linking

The onboarding flow captures:
- identity
- work authorization
- experience
- salary expectations
- preferred locations
- screening availability

---

### Provider System
Providers can:
- create company profiles
- manage job postings
- handle support requests
- coordinate hiring workflows

The provider flow supports:
- recruiter profiles
- company accounts
- hiring preference systems

---

### Admin Workspace
Admins manage:
- seekers
- providers
- jobs
- consultation requests

Admin systems include:
- approval workflows
- rejection flows
- meeting coordination
- full profile inspection
- status management

---

## Architecture

### Application Structure
The project uses:
- Next.js App Router
- API route segmentation
- modular dashboard systems
- reusable component architecture

Core architectural areas:
- onboarding systems
- role-based routing
- dashboard isolation
- protected APIs
- reusable UI layers

---

### Database Design
The database was designed around:
- relational user systems
- role isolation
- secure access patterns
- workflow coordination

Core tables:
- profiles
- seekers
- providers
- job_postings
- meetings
- requests
- applications
- documents

---

### Security Model
The project uses:
- Supabase Row Level Security
- role-based access control
- protected API routes
- isolated user visibility

Admins receive:
- cross-table visibility

Users are restricted to:
- their own records
- their own workflows

---

## Authentication System

Authentication uses:
- Supabase Auth
- role-based redirect systems
- automatic onboarding creation

Role assignment happens during signup and automatically initializes:
- seeker records
- provider records

through database triggers.

---

## UI & Design Philosophy

Steelcareer intentionally avoids:
- overly corporate interfaces
- sterile dashboard systems
- dense enterprise-style UI

The design direction focuses on:
- calm structure
- readable workflows
- soft modern interfaces
- reduced friction
- guided interaction

The platform attempts to make:
> career systems feel less emotionally exhausting.

---

## Interesting Technical Decisions

### Multi-Role Architecture
Instead of forcing all users into one dashboard, the system separates:
- seeker workflows
- provider workflows
- admin coordination

This keeps:
- interfaces focused
- permissions cleaner
- workflows easier to scale

---

### Human Coordination First
Most systems optimize for:
- automation
- recommendation engines
- AI ranking

Steelcareer intentionally optimizes for:
- coordination
- review
- structured communication
- trust-building

---

### Structured Onboarding
The onboarding system was designed to:
- progressively collect context
- reduce user overwhelm
- improve profile quality
- create structured candidate data

instead of:
- large static forms

---

## Challenges Faced

### Multi-Role System Complexity
Managing:
- auth flows
- dashboard routing
- database permissions
- API access
- onboarding state

across multiple user types introduced significant complexity.

---

### Schema Planning
The relational architecture required careful planning between:
- seekers
- providers
- applications
- meetings
- requests
- job systems

to avoid:
- permission conflicts
- scaling issues
- redundant data flows

---

### Production-Style Workflow Design
The project required thinking beyond:
- frontend screens

and into:
- real operational workflows
- admin tooling
- support handling
- request coordination
- hiring processes

---

## Learning Outcomes

The project helped build understanding of:
- production-style full-stack architecture
- role-based systems
- auth workflows
- database design
- relational schema planning
- onboarding UX
- API structure
- dashboard systems
- scalable frontend organization

It also strengthened:
- product thinking
- workflow design intuition
- real-world system planning

---

## Future Improvements

Potential future additions:
- recommendation systems
- intelligent candidate matching
- AI-assisted screening
- scheduling automation
- analytics dashboards
- recruiter insights
- communication systems
- notification infrastructure

---

## Current Status
Functional prototype / deployed platform.

Current focus areas:
- onboarding refinement
- workflow scaling
- production readiness
- UX improvements
- system expansion

---

## Product Direction

The larger vision behind Steelcareer is:
> building hiring systems that feel coordinated and human instead of algorithmically overwhelming.

The platform sits at the intersection of:
- recruitment
- workflow systems
- human coordination
- product infrastructure
- trust-based interaction

---

## Tags
nextjs, fullstack, recruitment-platform, supabase, role-based-auth, dashboard-system, workflow-design, hiring-platform, product-engineering, typescript