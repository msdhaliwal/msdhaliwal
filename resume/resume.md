---
name: Manpreet Singh Dhaliwal
title: Senior Backend Engineer & Technical Lead
location: Punjab, India · Remote (IST)
email: contact@msdhaliwal.com
phone: "+91 98888 45860"
website: msdhaliwal.com
linkedin: linkedin.com/in/msdhaliwal94
github: github.com/msdhaliwal
---

## Summary

Backend-leaning full-stack engineer with 8+ years building marketplaces, payments systems and developer tools in Node.js. I own how a product's server side is designed, built and kept healthy — clean schemas, sensible failure modes, and code that stays boring under load. I lead teams of 3–6 across dev and QA: running feasibility studies, turning vague requirements into scoped deliverables with product and design, mentoring engineers, and holding technical ownership of the architecture — while staying hands-on in the code.

## Experience

### Senior Software Engineer — Truck Parking Club
**Feb 2025 – Present · Remote · US truck-parking marketplace, ~260k active users**

- Own the server side of a two-sided marketplace serving **260,000+ active users at roughly 2 bookings a minute** — business logic, API design and performance, and the database schema behind landowners, drivers, fleet managers and admins.
- **Halved client API response times** by moving permission resolution into a Valkey (Redis-compatible) cache, and **cut admin dashboard load times to a third** with the same caching layer.
- Leading the move from a monolith to a hybrid microservices architecture — a pluggable notifications service (Twilio, SendGrid) and a bookings service decoupled from the order module.
- Run Stripe end to end: subscriptions, payment-method resolution, SetupIntent flows, subscription scheduling, and webhook handling for failed invoices and cancellations.
- Moved heavy work off the request path into BullMQ queues; shipped a React Native app for iOS and Android and integrated an AI voice/chat agent with short-lived-JWT session identity.
- Technical lead for a team of **5 (2 developers, 2 QA engineers and myself)**, reporting to the VP of Engineering and CTO: scoping, code review, mentoring and architecture decisions.

### Technical Lead — Truck Parking Club & Feasttt
**Jul 2022 – Feb 2025 · Codelux Technologies · Remote · product engineering for two client platforms**

- Replatformed Truck Parking Club off Sharetribe onto a custom Node.js backend, so listings, bookings, pricing, payouts and permissions could be designed around how truck parking actually works instead of a hosted marketplace template.
- Set the platform architecture the product still runs on three years later: schema, API surface, role-based organisations and payment flows.
- Led a team of 3–6 engineers across two products — mentoring, code review and technical ownership — and ran feasibility studies, scoping and delivery planning with cross-functional teams.
- Delivered Feasttt, an order-management platform for fine-dining restaurants, covering reservations, staff, orders, payments, refunds and owner analytics.

### Lead Engineer — Jetmanlabs
**Apr 2021 – Jul 2022 · Hybrid · developer-tools startup**

- Led architecture, design and stack selection for the Jetman platform, an API-testing suite that lets engineers build and validate REST APIs end to end.
- Built the backend in Node.js and MongoDB on Google Cloud.
- Chose Electron for the desktop client, shipping macOS, Windows and Linux from a single codebase.
- Acted as full-stack engineer across several products and set the engineering practices the team grew into.

### Founding Engineer — Jetmanlabs
**Sep 2018 – Apr 2021 · Hybrid · first engineering hire**

- Designed and built the backend infrastructure the company's later products were built on, with Node.js, MongoDB, Firebase and Stripe.
- Shipped the hard parts of client products: recurring payments, role-based access control and webhook event systems.
- Worked closely with the front-end team so API contracts, auth and data models fit together cleanly.

## Selected Projects

### Truck Parking Club — truck parking marketplace
Property owners list parking with location, size and pricing and accept bookings instantly; drivers and fleets book hourly to monthly by proximity, duration and cost; admins manage refunds, users, coupons and listings. Role-based organisations (owner, manager, guard, driver), dynamic pricing by time window and vehicle type, Stripe subscriptions and payouts, real-time booking notifications, and revenue reporting for owners.

*Node.js · Express · TypeScript · PostgreSQL · Sequelize · Valkey/Redis · BullMQ · Stripe · AWS · Cloudflare R2 · React · React Native*

### Feasttt — restaurant order management
Operations platform for fine dining: reservations, host and waiter management, orders, payments, refunds and reviews. Owner dashboards track sales, customer feedback and item ratings; admin analytics drive discount coupons for repeat customers and performance-based platform-fee discounts.

*Node.js · Payments · Analytics*

### Jetman App — local-first API client
A free alternative to Postman, built with Electron for macOS, Windows and Linux. Custom headers, authorization and response history, with every request stored on the user's machine — no cloud sync, no subscription.

*Electron · Node.js*

### Jetman CLI — API testing from the terminal
Companion CLI covering all common HTTP methods, with scripting and batch runs for shell-first workflows and CI/CD pipelines.

*Node.js · CLI · CI/CD*

## Skills

**Backend** — Node.js, TypeScript, Express, Sequelize, BullMQ, REST & GraphQL API design, authentication & RBAC, webhooks, microservices, backend development

**Databases & Data** — PostgreSQL, Valkey/Redis, MongoDB, Firebase, SQL, schema design, caching strategies

**Cloud & DevOps** — AWS (S3, Lambda, RDS, CloudFront, SES, SNS, SQS), Cloudflare R2, Google Cloud, PM2, Git, CI/CD

**Frontend & Desktop** — React, Vite, React Native, Electron, Tailwind, CSS

**Payments & Integrations** — Stripe, Twilio, SendGrid, HubSpot, Mailchimp, Beehiiv

**Leadership** — system design, team leadership (3–6 engineers), mentoring, feasibility studies, scoping & planning, cross-functional delivery, code review

## Education

**B.Tech, Computer Science & Engineering** — Punjab Technical University, 2014 – 2018
