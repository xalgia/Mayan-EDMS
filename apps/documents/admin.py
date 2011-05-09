from django.contrib import admin

from documents.models import MetadataType, DocumentType, Document, \
    MetadataSet, MetadataSetItem, DocumentMetadata, \
    DocumentTypeFilename, MetadataIndex, DocumentPage, MetadataGroup, \
    MetadataGroupItem, DocumentPageTransformation, RecentDocument

from filesystem_serving.admin import DocumentMetadataIndexInline


class MetadataTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'default', 'lookup')


class MetadataIndexInline(admin.StackedInline):
    model = MetadataIndex
    extra = 1
    classes = ('collapse-open',)
    allow_add = True


class MetadataSetItemInline(admin.StackedInline):
    model = MetadataSetItem
    extra = 1
    classes = ('collapse-open',)
    allow_add = True


class DocumentTypeFilenameInline(admin.StackedInline):
    model = DocumentTypeFilename
    extra = 1
    classes = ('collapse-open',)
    allow_add = True


class DocumentTypeAdmin(admin.ModelAdmin):
    inlines = [
        DocumentTypeFilenameInline, MetadataIndexInline
    ]


class DocumentMetadataInline(admin.StackedInline):
    model = DocumentMetadata
    extra = 0
    classes = ('collapse-open',)
    allow_add = False


class DocumentPageTransformationAdmin(admin.ModelAdmin):
    model = DocumentPageTransformation


class DocumentPageInline(admin.StackedInline):
    model = DocumentPage
    extra = 1
    classes = ('collapse-open',)
    allow_add = True


class DocumentAdmin(admin.ModelAdmin):
    inlines = [
        DocumentMetadataInline, DocumentMetadataIndexInline,
        DocumentPageInline
    ]
    list_display = ('uuid', 'file_filename', 'file_extension')


class MetadataGroupItemInline(admin.StackedInline):
    model = MetadataGroupItem
    extra = 1
    classes = ('collapse-open',)
    allow_add = True


class MetadataGroupAdmin(admin.ModelAdmin):
    inlines = [MetadataGroupItemInline]
    filter_horizontal = ['document_type']


class RecentDocumentAdmin(admin.ModelAdmin):
    model = RecentDocument
    list_display = ('user', 'document', 'datetime_accessed')
    readonly_fields = ('user', 'document', 'datetime_accessed')
    list_filter = ('user',)
    date_hierarchy = 'datetime_accessed'


class MetadataSetAdmin(admin.ModelAdmin):
    inlines = [MetadataSetItemInline]
    #filter_horizontal = ['document_type']    


admin.site.register(MetadataType, MetadataTypeAdmin)
admin.site.register(DocumentType, DocumentTypeAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(MetadataGroup, MetadataGroupAdmin)
admin.site.register(DocumentPageTransformation,
    DocumentPageTransformationAdmin)
admin.site.register(RecentDocument, RecentDocumentAdmin)
admin.site.register(MetadataSet, MetadataSetAdmin)
