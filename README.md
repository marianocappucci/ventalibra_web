# VentaLibra — Sitio Web / Landing

Landing page de marketing para [VentaLibra](https://ventalibra.com.ar), punto
de venta y gestión para comercios de retail (despensas, autoservicios,
comercios de alimentos, tiendas de ropa). Mismo patrón que
`contalibra_web`/`restolibra_web`/`gestiolibra_web`/`medlibra_web`: HTML
estático servido por nginx en un contenedor Docker.

## Estado actual (scaffold inicial)

- Landing completa: hero, módulos con badges por plan, rubros objetivo, cómo
  funciona, planes y precios, CTA de contacto y footer con el resto de la
  familia Libra.
- **Todavía sin**: documentación técnica gateada por login (`/docs/`, patrón
  de `contalibra_web`), CI/CD (GitHub Actions), y deploy al VPS. Queda para
  una ronda siguiente, una vez validado el contenido de la landing.

## Desarrollo local

```bash
docker compose build
docker compose up -d
```

Sirve en `http://localhost:8085`.

## Estructura

```
public/
  index.html          — Landing completa
  css/style.css        — Estilos (Inter + Bootstrap Icons via CDN)
  img/                  — (vacío por ahora, sin foto de hero propia)
Dockerfile              — FROM nginx:1.27-alpine
nginx.conf              — gzip, try_files, headers de seguridad
docker-compose.yml      — servicio web, red stack_stack-net (VPS Donweb)
```

## Relacionado

- Producto documentado: [VentaLibra](https://github.com/marianocappucci/ventalibra)
- Mismo patrón: `contalibra_web`, `restolibra_web`, `gestiolibra_web`, `medlibra_web`
