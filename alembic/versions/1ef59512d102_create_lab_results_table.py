"""create lab_results table

Revision ID: 1ef59512d102
Revises: e9e2cd8d651e
Create Date: 2025-01-28 23:04:22.676584

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1ef59512d102'
down_revision: Union[str, None] = 'e9e2cd8d651e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'lab_results',
        sa.Column('result_id', sa.Integer, nullable=False),
        sa.Column('test_id', sa.Integer, nullable=False),
        sa.Column('result_value', sa.Float, nullable=True),  # Double is equivalent to Float in SQLAlchemy
        sa.Column('result_unit', sa.Text, nullable=True),
        sa.Column('reference_range', sa.Text, nullable=True),
        sa.Column('result_status', sa.Text, nullable=True),
        sa.Column('performed_date', sa.Text, nullable=True),
        sa.Column('performed_time', sa.Text, nullable=True),
        sa.Column('reviewing_physician', sa.Text, nullable=True),

        # Primary key
        sa.PrimaryKeyConstraint('result_id'),

        # Add index with length for TEXT columns
        sa.Index(
            'idx_performed_date_time',
            'performed_date',
            'performed_time',
            mysql_length={'performed_date': 200, 'performed_time': 200}  # Limit length of TEXT columns in index
        )
    )


def downgrade():
    op.drop_table('lab_results')