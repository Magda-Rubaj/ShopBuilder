"""Create product table

Revision ID: 7b5a95cae1e5
Revises: 
Create Date: 2022-10-18 21:02:35.160089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b5a95cae1e5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "products",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String),
        sa.Column("price", sa.Float),
        sa.Column("image", sa.String, nullable=True),
        sa.Column("stock", sa.Integer),
        sa.Column("description", sa.String, nullable=True),
    )

def downgrade() -> None:
    op.drop_table("products")
