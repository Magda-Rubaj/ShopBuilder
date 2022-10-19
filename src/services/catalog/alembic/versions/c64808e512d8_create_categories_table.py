"""Create categories table

Revision ID: c64808e512d8
Revises: 7b5a95cae1e5
Create Date: 2022-10-19 18:41:28.867693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c64808e512d8'
down_revision = '7b5a95cae1e5'
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
