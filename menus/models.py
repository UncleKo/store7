from django.db import models
from django.template.defaultfilters import slugify
# from django_extensions.db.fields import AutoSlugField

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, PageChooserPanel #StreamFieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.core.models import Orderable


class MenuItem(Orderable):

  page = ParentalKey("Menu", related_name="menu_items")
  
  link_url = models.CharField(max_length=500, blank=True)
  link_page = models.ForeignKey(
    "wagtailcore.Page",
    null=True,
    blank=True,
    related_name="+",
    on_delete=models.CASCADE,
  )
  link_title = models.CharField(max_length=50, blank=True, null=True, verbose_name="Title(Option)", help_text="リンク先のページタイトルとは別のリンク名を付けたい時のみ")
  open_in_new_tab = models.BooleanField(default=False, blank=True)

  panels = [
    PageChooserPanel("link_page"),
    FieldPanel("link_url"),
    FieldPanel("link_title"),
    FieldPanel("open_in_new_tab"),
  ]

  @property
  def link(self):
  # def link(self) -> str:  ## to always return string
    if self.link_page:
      return self.link_page.url
    elif self.link_url:
      return self.link_url
    return '#'

  @property
  def title(self):
    if self.link_page and not self.link_title:
      return self.link_page.title
    elif self.link_title:
      return self.link_title
    return 'Missing Title'


# @register_snippet
class Menu(ClusterableModel):
  """The main menu clusterable model."""

  title = models.CharField(max_length=100)
  slug = models.SlugField(max_length=255)

  panels = [
    MultiFieldPanel([
      FieldPanel("title"), 
      # FieldPanel("slug"),
    ], heading="Menu"),
    InlinePanel("menu_items", label="Menu Item")
  ]

  # slugを自動的に作成
  def save(self, *args, **kwargs):
      # 作成時のみ（後でTitleが変わっても、URL変わらないように）
      if not self.id:
          self.slug = slugify(self.title)
      super(Menu, self).save(*args, **kwargs)


  def __str__(self):
    return self.title
