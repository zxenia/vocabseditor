from dal import autocomplete
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Div, MultiField, HTML, ButtonHolder
from crispy_forms.bootstrap import *
from .models import *
from django.forms.models import inlineformset_factory
from .custom_layout_object import *
from mptt.forms import TreeNodeChoiceField

class GenericFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(GenericFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.add_input(Submit('Filter', 'search'))


class UploadFileForm(forms.Form):
    file = forms.FileField()

    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'import'),)


######################################################################
#   Classes  to store titles and descriptions for ConceptScheme
######################################################################

class ConceptSchemeTitleForm(forms.ModelForm):

    class Meta:
        model = ConceptSchemeTitle
        exclude = ()


ConceptSchemeTitleFormSet = inlineformset_factory(
    SkosConceptScheme, ConceptSchemeTitle,
    form=ConceptSchemeTitleForm,
    fields=['name', 'language'], extra=1, can_delete=True
    )


class ConceptSchemeDescriptionForm(forms.ModelForm):

    class Meta:
        model = ConceptSchemeDescription
        exclude = ()


ConceptSchemeDescriptionFormSet = inlineformset_factory(
    SkosConceptScheme, ConceptSchemeDescription,
    form=ConceptSchemeDescriptionForm,
    fields=['name', 'language'], extra=1, can_delete=True
    )


class ConceptSchemeSourceForm(forms.ModelForm):

    class Meta:
        model = ConceptSchemeSource
        exclude = ()


ConceptSchemeSourceFormSet = inlineformset_factory(
    SkosConceptScheme, ConceptSchemeSource, form=ConceptSchemeSourceForm,
    fields=['name', 'language'],
    extra=1, can_delete=True
    )


######################################################################
#
# SkosConceptScheme
#
######################################################################


class SkosConceptSchemeForm(forms.ModelForm):

    class Meta:
        model = SkosConceptScheme
        exclude = ['created_by', ]
        widgets = {
            'curator': autocomplete.ModelSelect2Multiple(
                url='vocabs-ac:user-autocomplete'),
        }

    def __init__(self, *args, **kwargs):
        super(SkosConceptSchemeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('title'),
                Field('title_lang'),
                Fieldset('Add titles in other languages',
                    Formset('titles'))
                ,
                Fieldset('Add description',
                    Formset('descriptions'))
                ,
                Field('indentifier'),
                Field('language'),
                Field('creator'),
                Field('contributor'),
                Field('publisher'),
                Field('license'),
                Field('owner'),
                Field('subject'),
                Field('relation'),
                Field('coverage'),
                Fieldset('Add source information',
                    Formset('sources'))
                ,
                Field('version'),
                Field('legacy_id'),
                Field('date_issued'),
                Field('curator'),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')),
            )
            )
        self.helper.render_required_fields = True


class SkosConceptSchemeFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(SkosConceptSchemeFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                '',
                'title',
                'creator',
                css_id="basic_search_fields"
                ),
            )


######################################################################
#   Classes  to store labels and notes for Collection
######################################################################

class CollectionLabelForm(forms.ModelForm):

    class Meta:
        model = CollectionLabel
        exclude = ()


CollectionLabelFormSet = inlineformset_factory(
    SkosCollection, CollectionLabel, form=CollectionLabelForm,
    fields=['name', 'label_type', 'language'],
    extra=1, can_delete=True
    )


class CollectionNoteForm(forms.ModelForm):

    class Meta:
        model = CollectionNote
        exclude = ()


CollectionNoteFormSet = inlineformset_factory(
    SkosCollection, CollectionNote, form=CollectionNoteForm,
    fields=['name', 'note_type', 'language'],
    extra=1, can_delete=True
    )


class CollectionSourceForm(forms.ModelForm):

    class Meta:
        model = CollectionSource
        exclude = ()


CollectionSourceFormSet = inlineformset_factory(
    SkosCollection, CollectionSource, form=CollectionSourceForm,
    fields=['name', 'language'],
    extra=1, can_delete=True
    )

######################################################################
#
# SkosCollection
#
######################################################################

class SkosCollectionForm(forms.ModelForm):
    class Meta:
        model = SkosCollection
        exclude = ['created_by', ]
        widgets ={
            'scheme': autocomplete.ModelSelect2(
                url='vocabs-ac:skosconceptscheme-autocomplete'),
        }

    def __init__(self, *args, **kwargs):
        super(SkosCollectionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('name'),
                Field('label_lang'),
                Fieldset('Add more labels in other languages',
                    Formset('labels'))
                ,
                Field('scheme'),
                Field('creator'),
                Field('contributor'),
                Field('legacy_id'),
                Fieldset('Add more documentary notes',
                    Formset('notes'))
                ,
                Fieldset('Add source information',
                    Formset('sources'))
                ,
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')),
            )
            )
        self.helper.render_required_fields = True



class SkosCollectionFormHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super(SkosCollectionFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                '',
                'name',
                'creator',
                'scheme',
                'has_members__pref_label',
                css_id="basic_search_fields"
                ),
            )


######################################################################
#   Classes  to store labels, notes and sources for Concept
######################################################################

class ConceptLabelForm(forms.ModelForm):

    class Meta:
        model = ConceptLabel
        exclude = ()


ConceptLabelFormSet = inlineformset_factory(
    SkosConcept, ConceptLabel, form=ConceptLabelForm,
    fields=['name', 'label_type', 'language'],
    extra=1, can_delete=True
    )


class ConceptNoteForm(forms.ModelForm):

    class Meta:
        model = ConceptNote
        exclude = ()


ConceptNoteFormSet = inlineformset_factory(
    SkosConcept, ConceptNote, form=ConceptNoteForm,
    fields=['name', 'note_type', 'language'],
    extra=1, can_delete=True
    )


class ConceptSourceForm(forms.ModelForm):

    class Meta:
        model = ConceptSource
        exclude = ()


ConceptSourceFormSet = inlineformset_factory(
    SkosConcept, ConceptSource, form=ConceptSourceForm,
    fields=['name', 'language'],
    extra=1, can_delete=True
    )


######################################################################
#
# SkosConcept
#
######################################################################

class SkosConceptForm(forms.ModelForm):
    broader_concept = TreeNodeChoiceField(
        queryset=SkosConcept.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='vocabs-ac:skosconcept-nobroaderterm-autocomplete',
            forward=['scheme']
        ),
        help_text="A concept with a broader meaning that a current concept inherits from",
        required=False
    )
    collection = forms.ModelMultipleChoiceField(
        queryset=SkosCollection.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(
                url='vocabs-ac:skoscollection-autocomplete',
                forward=['scheme']
        ),
        help_text="member of skos:Collection",
        required=False
    )

    class Meta:
        model = SkosConcept
        exclude = ['created_by', ]
        widgets = {
            'scheme': autocomplete.ModelSelect2(
                url='vocabs-ac:skosconceptscheme-autocomplete'),
            'skos_related': autocomplete.ModelSelect2Multiple(
                url='vocabs-ac:skosconcept-nobroaderterm-autocomplete'),
            'skos_broadmatch': autocomplete.ModelSelect2Multiple(
                url='vocabs-ac:skosconcept-nobroaderterm-autocomplete'),
            'skos_narrowmatch': autocomplete.ModelSelect2Multiple(
                url='vocabs-ac:skosconcept-nobroaderterm-autocomplete'),
            'skos_exactmatch': autocomplete.ModelSelect2Multiple(
                url='vocabs-ac:skosconcept-nobroaderterm-autocomplete'),
            'skos_relatedmatch': autocomplete.ModelSelect2Multiple(
                url='vocabs-ac:skosconcept-nobroaderterm-autocomplete'),
            'skos_closematch': autocomplete.ModelSelect2Multiple(
                url='vocabs-ac:skosconcept-nobroaderterm-autocomplete'),
        }

    # class Media:
    #     js = ('autocomplete.init.js')


    def __init__(self, *args, **kwargs):
        super(SkosConceptForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('pref_label'),
                Field('pref_label_lang'),
                Fieldset('Add more labels',
                    Formset('labels'))
                ,
                Field('scheme'),
                Field('top_concept'),
                Field('collection'),
                Field('broader_concept'),
                Fieldset('Add documentary notes',
                    Formset('notes'))
                ,
                Field('creator'),
                Field('contributor'),
                Field('same_as_external'),
                Field('notation'),
                Fieldset('Add source information',
                    Formset('sources'))
                ,
                Accordion(
                AccordionGroup(
                    'Add SKOS semantic relationships',
                    'skos_related',
                    'skos_broadmatch',
                    'skos_narrowmatch',
                    'skos_exactmatch',
                    'skos_relatedmatch',
                    'skos_closematch',
                    'legacy_id',
                    css_id="advanced_skos_fields"
                ),
                ),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')),
            )
            )
        self.helper.render_required_fields = True


class SkosConceptFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(SkosConceptFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'pref_label',
                'scheme',
                'collection',
                'broader_concept',
                css_id="basic_search_fields"
                ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    'top_concept',
                    'pref_label_lang',
                    css_id="more"
                    ),
                )
            )
