"""create lab_tests table

Revision ID: e9e2cd8d651e
Revises: 9374fd1d9aa4
Create Date: 2025-01-28 23:03:55.092257

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e9e2cd8d651e'
down_revision: Union[str, None] = '9374fd1d9aa4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'lab_tests',
        sa.Column('test_id', sa.Integer, nullable=False),
        sa.Column('patient_id', sa.Integer, nullable=False),
        sa.Column('test_name', sa.Text, nullable=True),
        sa.Column('order_date', sa.Text, nullable=True),
        sa.Column('order_time', sa.Text, nullable=True),
        sa.Column('ordering_physician', sa.Text, nullable=True),

        # Primary key
        sa.PrimaryKeyConstraint('test_id'),

        # Add index with length for TEXT columns
        sa.Index(
            'idx_order_date_time',
            'order_date',
            'order_time',
            mysql_length={'order_date': 200, 'order_time': 200}  # Limit length of TEXT columns in index
        )
    )


def downgrade():
    op.drop_table('lab_tests')