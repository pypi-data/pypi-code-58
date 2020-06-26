# Generated by Django 3.0.6 on 2020-06-22 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ArvRegimens",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        help_text="This is the stored value, required",
                        max_length=250,
                        unique=True,
                        verbose_name="Stored value",
                    ),
                ),
                (
                    "display_name",
                    models.CharField(
                        db_index=True,
                        help_text="(suggest 40 characters max.)",
                        max_length=250,
                        unique=True,
                        verbose_name="Name",
                    ),
                ),
                (
                    "display_index",
                    models.IntegerField(
                        db_index=True,
                        default=0,
                        help_text="Index to control display order if not alphabetical, not required",
                        verbose_name="display index",
                    ),
                ),
                (
                    "field_name",
                    models.CharField(
                        blank=True,
                        editable=False,
                        help_text="Not required",
                        max_length=25,
                        null=True,
                    ),
                ),
                (
                    "version",
                    models.CharField(default="1.0", editable=False, max_length=35),
                ),
            ],
            options={
                "verbose_name": "ARV Regimens",
                "verbose_name_plural": "ARV Regimens",
                "ordering": ["display_index", "display_name"],
                "abstract": False,
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
            },
        ),
        migrations.CreateModel(
            name="Conditions",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        help_text="This is the stored value, required",
                        max_length=250,
                        unique=True,
                        verbose_name="Stored value",
                    ),
                ),
                (
                    "display_name",
                    models.CharField(
                        db_index=True,
                        help_text="(suggest 40 characters max.)",
                        max_length=250,
                        unique=True,
                        verbose_name="Name",
                    ),
                ),
                (
                    "display_index",
                    models.IntegerField(
                        db_index=True,
                        default=0,
                        help_text="Index to control display order if not alphabetical, not required",
                        verbose_name="display index",
                    ),
                ),
                (
                    "field_name",
                    models.CharField(
                        blank=True,
                        editable=False,
                        help_text="Not required",
                        max_length=25,
                        null=True,
                    ),
                ),
                (
                    "version",
                    models.CharField(default="1.0", editable=False, max_length=35),
                ),
            ],
            options={
                "verbose_name": "Conditions",
                "verbose_name_plural": "Conditions",
                "ordering": ["display_index", "display_name"],
                "abstract": False,
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
            },
        ),
        migrations.CreateModel(
            name="DiabetesTreatment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        help_text="This is the stored value, required",
                        max_length=250,
                        unique=True,
                        verbose_name="Stored value",
                    ),
                ),
                (
                    "display_name",
                    models.CharField(
                        db_index=True,
                        help_text="(suggest 40 characters max.)",
                        max_length=250,
                        unique=True,
                        verbose_name="Name",
                    ),
                ),
                (
                    "display_index",
                    models.IntegerField(
                        db_index=True,
                        default=0,
                        help_text="Index to control display order if not alphabetical, not required",
                        verbose_name="display index",
                    ),
                ),
                (
                    "field_name",
                    models.CharField(
                        blank=True,
                        editable=False,
                        help_text="Not required",
                        max_length=25,
                        null=True,
                    ),
                ),
                (
                    "version",
                    models.CharField(default="1.0", editable=False, max_length=35),
                ),
            ],
            options={
                "verbose_name": "Diabetes Treatment",
                "verbose_name_plural": "Diabetes Treatment",
                "ordering": ["display_index", "display_name"],
                "abstract": False,
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
            },
        ),
        migrations.CreateModel(
            name="HypertensionTreatment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        help_text="This is the stored value, required",
                        max_length=250,
                        unique=True,
                        verbose_name="Stored value",
                    ),
                ),
                (
                    "display_name",
                    models.CharField(
                        db_index=True,
                        help_text="(suggest 40 characters max.)",
                        max_length=250,
                        unique=True,
                        verbose_name="Name",
                    ),
                ),
                (
                    "display_index",
                    models.IntegerField(
                        db_index=True,
                        default=0,
                        help_text="Index to control display order if not alphabetical, not required",
                        verbose_name="display index",
                    ),
                ),
                (
                    "field_name",
                    models.CharField(
                        blank=True,
                        editable=False,
                        help_text="Not required",
                        max_length=25,
                        null=True,
                    ),
                ),
                (
                    "version",
                    models.CharField(default="1.0", editable=False, max_length=35),
                ),
            ],
            options={
                "verbose_name": "Hypertension Treatment",
                "verbose_name_plural": "Hypertension Treatment",
                "ordering": ["display_index", "display_name"],
                "abstract": False,
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
            },
        ),
        migrations.CreateModel(
            name="OffstudyReasons",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        help_text="This is the stored value, required",
                        max_length=250,
                        unique=True,
                        verbose_name="Stored value",
                    ),
                ),
                (
                    "display_name",
                    models.CharField(
                        db_index=True,
                        help_text="(suggest 40 characters max.)",
                        max_length=250,
                        unique=True,
                        verbose_name="Name",
                    ),
                ),
                (
                    "display_index",
                    models.IntegerField(
                        db_index=True,
                        default=0,
                        help_text="Index to control display order if not alphabetical, not required",
                        verbose_name="display index",
                    ),
                ),
                (
                    "field_name",
                    models.CharField(
                        blank=True,
                        editable=False,
                        help_text="Not required",
                        max_length=25,
                        null=True,
                    ),
                ),
                (
                    "version",
                    models.CharField(default="1.0", editable=False, max_length=35),
                ),
            ],
            options={
                "verbose_name": "Offstudy Reasons",
                "verbose_name_plural": "Offstudy Reasons",
                "ordering": ["display_index", "display_name"],
                "abstract": False,
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
            },
        ),
        migrations.CreateModel(
            name="VisitReasons",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True,
                        help_text="This is the stored value, required",
                        max_length=250,
                        unique=True,
                        verbose_name="Stored value",
                    ),
                ),
                (
                    "display_name",
                    models.CharField(
                        db_index=True,
                        help_text="(suggest 40 characters max.)",
                        max_length=250,
                        unique=True,
                        verbose_name="Name",
                    ),
                ),
                (
                    "display_index",
                    models.IntegerField(
                        db_index=True,
                        default=0,
                        help_text="Index to control display order if not alphabetical, not required",
                        verbose_name="display index",
                    ),
                ),
                (
                    "field_name",
                    models.CharField(
                        blank=True,
                        editable=False,
                        help_text="Not required",
                        max_length=25,
                        null=True,
                    ),
                ),
                (
                    "version",
                    models.CharField(default="1.0", editable=False, max_length=35),
                ),
            ],
            options={
                "verbose_name": "Visit Reasons",
                "verbose_name_plural": "Visit Reasons",
                "ordering": ["display_index", "display_name"],
                "abstract": False,
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
            },
        ),
        migrations.AddIndex(
            model_name="visitreasons",
            index=models.Index(
                fields=["id", "display_name", "display_index"],
                name="inte_lists__id_d40cbd_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="offstudyreasons",
            index=models.Index(
                fields=["id", "display_name", "display_index"],
                name="inte_lists__id_fbf932_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="hypertensiontreatment",
            index=models.Index(
                fields=["id", "display_name", "display_index"],
                name="inte_lists__id_3c3712_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="diabetestreatment",
            index=models.Index(
                fields=["id", "display_name", "display_index"],
                name="inte_lists__id_fa78d2_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="conditions",
            index=models.Index(
                fields=["id", "display_name", "display_index"],
                name="inte_lists__id_663473_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="arvregimens",
            index=models.Index(
                fields=["id", "display_name", "display_index"],
                name="inte_lists__id_f97923_idx",
            ),
        ),
    ]
