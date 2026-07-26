# VentaLibra — Sitio Web / Landing

Landing page de marketing para [VentaLibra](https://ventalibra.com.ar), punto
de venta y gestión para comercios de retail (despensas, autoservicios,
comercios de alimentos, tiendas de ropa). Mismo patrón que
`contalibra_web`/`restolibra_web`/`gestiolibra_web`/`medlibra_web`: HTML
estático servido por nginx en un contenedor Docker.

## Estado actual

- Landing completa: hero, módulos con badges por plan, rubros objetivo, cómo
  funciona, planes y precios, CTA de contacto y footer con el resto de la
  familia Libra.
- **Documentación técnica en `/docs/`** (12 páginas), gateada por login real
  contra la instancia del cliente — mismo patrón que `contalibra_web`, con una
  diferencia: como VentaLibra no tiene un backoffice con `/api/clientes-publicos`,
  el login pide directamente el **subdominio** en vez de un `<select>`.
- **CI/CD** (`.github/workflows/deploy.yml`): push a `main` dispara rsync al
  VPS + rebuild de Docker. Requiere el secret `VPS_DEPLOY_KEY` cargado en el
  repo (no incluido — mismo criterio que el resto de la familia).
- **Todavía sin**: primer deploy real al VPS, ni proxy NPM/SSL para el apex
  `ventalibra.com.ar` (hoy solo existe para `dev.ventalibra.com.ar`, la app).

## Desarrollo local

```bash
docker compose build
docker compose up -d
```

Sirve en `http://localhost:8085` (requiere la red externa `stack_stack-net` —
en el VPS ya existe; en local hay que crearla con
`docker network create stack_stack-net` para levantar el stack completo).

## Acceso a /docs/ (login-docs)

El backend `auth/` valida en tiempo real contra `https://{subdominio}.ventalibra.com.ar/auth/verify`
(nuevo endpoint necesario del lado de la app, ver `ventalibra` repo) usando el
secreto compartido `DOCS_AUTH_SECRET`. No hay tabla de usuarios propia acá.

## Estructura

```
public/
  index.html          — Landing completa
  css/style.css        — Estilos (Inter + Bootstrap Icons via CDN)
  img/                  — (vacío por ahora, sin foto de hero propia)
  docs/                 — 12 páginas HTML de documentación (gateadas)
auth/                  — Backend FastAPI de acceso a /docs/
  app.py                — /login-docs, /check, /logout-docs
  Dockerfile            — python:3.12-slim
  requirements.txt
Dockerfile              — FROM nginx:1.27-alpine
nginx.conf              — gzip, try_files, auth_request sobre /docs/, headers de seguridad
docker-compose.yml      — servicios web (8085:80) + auth (interno), red stack_stack-net
.github/workflows/
  deploy.yml            — CI/CD rsync al VPS + docker compose rebuild
```

## Relacionado

- Producto documentado: [VentaLibra](https://github.com/marianocappucci/ventalibra)
- Mismo patrón: `contalibra_web`, `restolibra_web`, `gestiolibra_web`, `medlibra_web`
