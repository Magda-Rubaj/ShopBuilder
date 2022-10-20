"""Add products table

Revision ID: e870594faf1a
Revises: 4d2551229701
Create Date: 2022-10-20 22:12:38.358576

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'e870594faf1a'
down_revision = '4d2551229701'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "products",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String),
        sa.Column("price", postgresql.JSONB()),
        sa.Column("image", sa.String, nullable=True),
        sa.Column("stock", sa.Integer),
        sa.Column("description", sa.String, nullable=True),
        sa.Column("category", sa.Integer, sa.ForeignKey("categories.id"))
    )

def downgrade() -> None:
    op.drop_table("products")
    
