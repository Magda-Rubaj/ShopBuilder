"""Add categories table

Revision ID: 4d2551229701
Revises: 
Create Date: 2022-10-20 22:11:56.645633

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d2551229701'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "categories",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String),
        sa.Column("level", sa.Integer),
        sa.Column("parent", sa.ForeignKey("categories.id"), nullable=True),

    )


def downgrade() -> None:
    op.drop_table("categories")
