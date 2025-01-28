"""create patient_information table

Revision ID: 5490359a3c0c
Revises: 1ef59512d102
Create Date: 2025-01-28 23:04:58.738749

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5490359a3c0c'
down_revision: Union[str, None] = '1ef59512d102'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'patient_information',
        sa.Column('patient_id', sa.Integer, nullable=False),
        sa.Column('first_name', sa.Text, nullable=True),
        sa.Column('last_name', sa.Text, nullable=True),
        sa.Column('date_of_birth', sa.Text, nullable=True),
        sa.Column('primary_physician', sa.Text, nullable=True),
        sa.Column('insurance_provider', sa.Text, nullable=True),
        sa.Column('blood_type', sa.Text, nullable=True),
        sa.Column('allergies', sa.Text, nullable=True),

        # Primary key
        sa.PrimaryKeyConstraint('patient_id')
    )


def downgrade():
    op.drop_table('patient_information')