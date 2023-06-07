"""added tables

Revision ID: 52aa23bd7a67
Revises: 7c9d48566ea1
Create Date: 2023-06-07 19:09:47.540478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52aa23bd7a67'
down_revision = '7c9d48566ea1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('parents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teachers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('class_in', sa.Integer(), nullable=True),
    sa.Column('age_in', sa.Integer(), nullable=True),
    sa.Column('position_in', sa.Integer(), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['parents.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teacher_parent',
    sa.Column('teacher_id', sa.Integer(), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['parent_id'], ['parents.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('teacher_id', 'parent_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teacher_parent')
    op.drop_table('students')
    op.drop_table('teachers')
    op.drop_table('parents')
    # ### end Alembic commands ###
