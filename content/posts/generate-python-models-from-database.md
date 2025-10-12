Title: Generating Python models from an existing database
Started: 2025-09-12 15:12:02
Date: 2025-09-12 16:42:19
Updated: 2025-09-12 18:03:00
Slug: generate-python-models-from-database
Location: Home office
Authors: Michiel Scholten
Status: published
Category: howto
Tags: dev, digimarks, energy, howto, link, python

If you have an existing database - for example from an older application, or a dataset you downloaded - and want to use it with Python, you might want to have SQLAlchemy ORM models for it for easier querying.

Enter [sqlacodegen](https://github.com/agronholm/sqlacodegen):

> This is a tool that reads the structure of an existing database and generates the appropriate SQLAlchemy model code, using the declarative style if possible.
>
> This tool was written as a replacement for [sqlautocode](http://code.google.com/p/sqlautocode/), which was suffering from several issues (including, but not limited to, incompatibility with Python 3 and the latest SQLAlchemy version).

This nifty tool supports the latest SQLAlchemy (2.x series) and produces nicely structured, declarative code. For example, the current version of my [digimarks](https://github.com/aquatix/digimarks) web-based bookmarking system has a sqlite database on which I performed a `sqlacodegen sqlite:///bookmarks.db` which immediately gave:

```python
from typing import Optional
import datetime

from sqlalchemy import Boolean, DateTime, Integer, String, Text, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass


class Bookmark(Base):
    __tablename__ = 'bookmark'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    userkey: Mapped[str] = mapped_column(String(255), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    url: Mapped[str] = mapped_column(String(255), nullable=False)
    created_date: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)
    url_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    tags: Mapped[str] = mapped_column(String(255), nullable=False)
    http_status: Mapped[int] = mapped_column(Integer, nullable=False)
    modified_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    favicon: Mapped[Optional[str]] = mapped_column(String(255))
    starred: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('0'))
    deleted_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('null'))
    status: Mapped[Optional[int]] = mapped_column(Integer, server_default=text('0'))
    note: Mapped[Optional[str]] = mapped_column(Text, server_default=text('null'))


class Publictag(Base):
    __tablename__ = 'publictag'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tagkey: Mapped[str] = mapped_column(String(255), nullable=False)
    userkey: Mapped[str] = mapped_column(String(255), nullable=False)
    tag: Mapped[str] = mapped_column(String(255), nullable=False)
    created_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('null'))


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(255), nullable=False)
    key: Mapped[str] = mapped_column(String(255), nullable=False)
    created_date: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False)
    theme: Mapped[Optional[str]] = mapped_column(String(20), server_default=text("'green'"))
```

That's pretty nice! It gives a nicely clean slate for generating an initial [alembic](https://alembic.sqlalchemy.org/en/latest/) migration, which I will need for my current rewrite of the bookmark system into [FastAPI](https://fastapi.tiangolo.com/) and [SQLModel](https://sqlmodel.tiangolo.com/). I don't *need* to change the database for that undertaking at this moment, but I would really like to clean things up a bit (read: fix some names, add a property and such) :)


## Bonus: generating (initial) alembic migration

To now generate an initial migration with [alembic](https://alembic.sqlalchemy.org/en/latest/)

```bash
# ls -1
> bookmarks.db

mkdir projecttmp
touch projecttmp/__init__.py

sqlacodegen sqlite:///bookmarks.db > projecttmp/models.py

alembic init alembic
```

Now edit `alembic.ini` to use `sqlalchemy.url = sqlalchemy://bookmarks.db` and `alembic/env.py` with the following:

```python
# Only added/changed lines shown here

# Add import of your models, including Base
from projecttmp.models import *

target_metadata = Base.metadata
```

Now, run a migration generator to check if a clean, no-changes migration is created:

```bash
alembic revision --autogenerate
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
  Generating projecttmp/alembic/versions/9252cf81e5f8_.py ...  done
```

This should result in something that looks like:

```python
"""empty message

Revision ID: 9252cf81e5f8
Revises:
Create Date: 2025-09-12 15:50:55.569519

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9252cf81e5f8'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
```

As you can see, the `upgrade()` migration is nicely empty, so the database compares cleanly with the models, as expected as we just generated the latter from the tables in that same database.

Now, remove this try-out migration so it won't interfere with the real initial migration we will be creating next:

```bash
# Use the hash-based filename of your own trial, alembic generates a random filename
rm alembic/versions/9252cf81e5f8_.py

# Next, move our real DB file out of the way:
mv bookmarks.db bookmarks.db_backup

# Create empty database with same name
sqlite3 bookmarks.db "VACUUM;"

# Do the migration again, but now alembic will compare the models against the empty DB
alembic revision --autogenerate -m "Initial migration"

INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'bookmark'
INFO  [alembic.autogenerate.compare] Detected added table 'publictag'
INFO  [alembic.autogenerate.compare] Detected added table 'user'
  Generating projecttmp/alembic/versions/115bcd2e1a38_initial_migration.py ...  done
```

For `digimarks` this gives:

```python
"""Initial migration

Revision ID: 115bcd2e1a38
Revises: 
Create Date: 2025-09-12 16:06:16.479075

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '115bcd2e1a38'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bookmark',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userkey', sa.String(length=255), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.Column('url_hash', sa.String(length=255), nullable=False),
    sa.Column('tags', sa.String(length=255), nullable=False),
    sa.Column('http_status', sa.Integer(), nullable=False),
    sa.Column('modified_date', sa.DateTime(), nullable=True),
    sa.Column('favicon', sa.String(length=255), nullable=True),
    sa.Column('starred', sa.Boolean(), server_default=sa.text('0'), nullable=True),
    sa.Column('deleted_date', sa.DateTime(), server_default=sa.text('(null)'), nullable=True),
    sa.Column('status', sa.Integer(), server_default=sa.text('0'), nullable=True),
    sa.Column('note', sa.Text(), server_default=sa.text('(null)'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('publictag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tagkey', sa.String(length=255), nullable=False),
    sa.Column('userkey', sa.String(length=255), nullable=False),
    sa.Column('tag', sa.String(length=255), nullable=False),
    sa.Column('created_date', sa.DateTime(), server_default=sa.text('(null)'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('key', sa.String(length=255), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.Column('theme', sa.String(length=20), server_default=sa.text("'green'"), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('publictag')
    op.drop_table('bookmark')
    # ### end Alembic commands ###
```

Good, that tracks the models just nicely.

Now, move this migration to your own project. The whole `migrations` directory can be moved if you want; don't forget the `alembic.ini`. Myself, I only copied over the migration file, as I already initialised `alembic` in my project with [`asyncio` support](https://alembic.sqlalchemy.org/en/latest/cookbook.html#using-asyncio-with-alembic) (`alembic init -t async migrations`).

You can now stamp the original database with this initial migration to let alembic know that the current migration represents the state of the database so next time you run `alembic upgrade head` it will begin from this migration:

```bash
# Probably first rename the old DB back to the original filename

# Use the hash from your own generated migration!
alembic stamp 115bcd2e1a38
```

If you now for example use the excellent [SQLiteBrowser](https://sqlitebrowser.org/) on the database, you'll notice the `alembic` table. From now on, we can use `alembic` to track changes and generate migrations:

```bash
# Generate a new migration after changes to your code
alembic revision --autogenerate -m "Fixes to the models"

# Apply the new migration to the database
alembic upgrade head
```

Happy hacking!
