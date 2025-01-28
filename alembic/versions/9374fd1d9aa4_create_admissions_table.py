"""create admissions table

Revision ID: 9374fd1d9aa4
Revises: 
Create Date: 2025-01-28 23:03:10.359079

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9374fd1d9aa4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'admissions',
        sa.Column('patient_id', sa.Integer, nullable=False),
        sa.Column('hospitalization_case_number', sa.Integer, nullable=True),
        sa.Column('admission_date', sa.Text, nullable=True),
        sa.Column('admission_time', sa.Text, nullable=True),
        sa.Column('release_date', sa.Text, nullable=True),
        sa.Column('release_time', sa.Text, nullable=True),
        sa.Column('department', sa.Text, nullable=True),
        sa.Column('room_number', sa.Text, nullable=True),
        sa.PrimaryKeyConstraint('patient_id'),
        sa.Index(
            'idx_admission_date_time',
            'admission_date',
            'admission_time',
            mysql_length={'admission_date': 200, 'admission_time': 200}  # Limit length of TEXT columns
        )
    )


def downgrade() -> None:
    op.drop_table('admissions')


