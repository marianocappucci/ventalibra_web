"""Backend de acceso a /docs/ para la landing de VentaLibra -- config sobre
libra_web_kit.docs_auth (extraído 2026-07-26, ver
wiki/analyses/auditoria-duplicacion-familia-libra.md)."""
from libra_web_kit.docs_auth import build_docs_login_app, DocsLoginTheme

app = build_docs_login_app(
    product_name="VentaLibra",
    apex_domain_default="ventalibra.com.ar",
    secret_key_env="DOCS_SESSION_SECRET",
    secret_key_default="ventalibra-docs-secret-change-me",
    verify_path="/auth/verify",
    slug_placeholder="tu-comercio",
    theme=DocsLoginTheme(accent="#d97706", accent_hover="#b45309"),
)
