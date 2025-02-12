"""empty message

Revision ID: 98a864ff0500
Revises: 
Create Date: 2025-01-29 16:53:11.310482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98a864ff0500'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('response',
    sa.Column('obj_id', sa.Integer(), nullable=False),
    sa.Column('date_responded', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('obj_id')
    )
    op.create_table('survey',
    sa.Column('obj_id', sa.Integer(), nullable=False),
    sa.Column('hash_key', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('obj_id'),
    sa.UniqueConstraint('hash_key'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('obj_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('obj_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('question',
    sa.Column('obj_id', sa.Integer(), nullable=False),
    sa.Column('survey_id', sa.Integer(), nullable=True),
    sa.Column('text', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['survey_id'], ['survey.obj_id'], ),
    sa.PrimaryKeyConstraint('obj_id')
    )
    op.create_table('responder_answer',
    sa.Column('response_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('question_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('answer', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['question_id'], ['question.obj_id'], ),
    sa.ForeignKeyConstraint(['response_id'], ['response.obj_id'], ),
    sa.PrimaryKeyConstraint('response_id', 'question_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('responder_answer')
    op.drop_table('question')
    op.drop_table('user')
    op.drop_table('survey')
    op.drop_table('response')
    # ### end Alembic commands ###
