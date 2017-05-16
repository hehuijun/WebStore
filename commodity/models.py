from django.db import models

# Create your models here.
class Commondity(models.Model):
    CommodityName=models.CharField(max_length=100) #商品名称
    CommodityCategory = models.CharField(max_length=50,blank= True) #商品类别
    CommodityPrice = models.DecimalField(max_digits=11,decimal_places=2)#商品价格
    CommondityImage = models.ImageField(upload_to='pic_folder', default = 'pic_folder/None/no-img.jpg')#商品图片

    CommodityDateTime = models.DateTimeField(auto_now_add= True) #发布日期
    CommodityContent = models.TextField(blank= True,null= True) #商品说明
    def __unicode__(self):
        return  self.CommodityName
    class Meta: #按时间下降排序
        ordering = ['-CommodityDateTime']

#class ArticleAdmin(admin.ModelAdmin):
 #   list_display = ('title','date_time')
