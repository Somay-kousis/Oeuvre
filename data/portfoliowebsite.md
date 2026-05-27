# portfolio

## Overview
A cinematic developer portfolio focused on immersive frontend experiences, spatial motion, and interaction-heavy UI systems. Built as both a personal website and an experimentation ground for advanced frontend rendering techniques.

---

## Purpose
The project was designed to explore how modern frontend technologies can create emotionally immersive digital experiences instead of static websites.

It focuses heavily on:
- motion systems
- WebGL rendering
- spatial interaction
- cinematic transitions
- layered visual feedback
- experimental UI behavior

---

## Core Features
- Live WebGL particle field using Three.js
- Scroll-reactive camera movement
- Animated wave-fill typography
- Blend-mode custom cursor system
- Scroll-sequenced project reveals
- Cinematic procedural noise overlay
- Blur-based page transitions
- Scroll-driven text reveal animations
- Lenis smooth scrolling
- Animated preloader experience

---

## Technical Stack
- Next.js 16
- React 19
- TypeScript
- TailwindCSS v4
- Framer Motion
- Three.js
- React Three Fiber
- WebGL
- Lenis

---

## Architecture
The application uses Next.js App Router with persistent layout rendering.

The WebGL scene remains mounted globally behind the application to avoid expensive remounting during navigation.

Animation systems are primarily driven using:
- Framer Motion motion values
- scroll transforms
- spring physics
- GPU compositing
- CSS blend modes

---

## Interesting Technical Decisions
### Volumetric Particle Distribution
Particle positions use cube-root randomization for true volumetric density instead of center clustering.

### Persistent WebGL Canvas
The particle field never unmounts across routes, creating spatial continuity throughout the experience.

### ClipPath Wave Animation
Project title hover effects use animated SVG clip paths instead of traditional masking techniques.

### Blend Mode Cursor
The custom cursor relies on `mix-blend-mode: difference` for automatic inversion against backgrounds.

### GPU-Friendly Motion
Most animations rely on transforms, opacity, and filters to avoid layout thrashing.

---

## Design Philosophy
The portfolio was intentionally designed to feel:
- cinematic
- atmospheric
- slightly futuristic
- emotionally immersive
- minimal but alive

The goal was to create something that feels closer to an interactive experience than a traditional developer portfolio.

---

## Performance Notes
- GPU-accelerated transforms
- Persistent rendering systems
- Optimized particle calculations
- Reduced layout recalculations
- Smooth scroll damping via Lenis
- Motion-value driven animations

---

## Deployment
Deployed using Vercel.

---

## Links
- Live Demo: https://portfolio-sable-psi-56.vercel.app/writing
- GitHub: https://github.com/Somay-kousis/portfolio

---

## Future Improvements
- Dynamic shader experimentation
- Interactive 3D project environments
- Audio-reactive systems
- AI-assisted personalization
- Advanced motion choreography

---

## Tags
frontend, nextjs, threejs, webgl, motion-design, ui-engineering, creative-development, immersive-ui, portfolio, animation