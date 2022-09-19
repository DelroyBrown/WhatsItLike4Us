# from location_field.models.plain import PlainLocationField, BaseLocationField
# from mapbox_location_field.spatial.models import SpatialLocationField
from secrets import choice
from mapbox_location_field.models import LocationField
from django.db import models


class MainContactModel(models.Model):
    STILL_EMPLOYED = (
        ('prefer_to_not_say', 'Prefer To Not Say'),
        ('blank_blank', '......'),
        ('still_employed', 'Still Employed Here'),
        ('no_longer_employed', 'No Longer Employed Here'),
    )
    TIME_EMPLOYED = (
        ('0_1_year', '0-1 Year'),
        ('1_3_years', '1-3 Years'),
        ('3_5_years', '3-5 Years'),
        ('5_10_years', '5-10 Year'),
        ('10_year_plus', '10+ Years'),
    )
    AWKWARDNESS_RATING = (
        ('1_5', '1/5'),
        ('2_5', '2/5'),
        ('3_5', '3/5'),
        ('4_5', '4/5'),
        ('5_5', '5/5'),
    )
    SEXUAL_ORIENTATION = (
        ('prefer_to_not_say', 'Prefer To Not Say'),
        ('blank_blank', '......'),
        ('Allosexual', 'Allosexual'),
        ('Androsexual', 'Androsexual'),
        ('Asexual', 'Asexual'),
        ('Autosexual', 'Autosexual'),
        ('Bi-curious', 'Bi-curious'),
        ('Bisexual', 'Bisexual'),
        ('Closeted', 'Closeted'),
        ('Demisexual', 'Demisexual'),
        ('Fluid', 'Fluid'),
        ('Gay', 'Gay'),
        ('Graysexual', ' Graysexual'),
        ('Gynesexual', ' Gynesexual'),
        ('Heterosexual/straight', ' Heterosexual/straight'),
        ('Homosexual', ' Homosexual'),
        ('Lesbian', 'Lesbian'),
        ('Pansexual', 'Pansexual'),
        ('Queer', 'Queer'),
        ('Questioning', 'Questioning'),
        ('Sapiosexual', 'Sapiosexual'),
        ('Sex-repulsed', 'Sex-repulsed'),
        ('Skoliosexual', 'Skoliosexual'),
        ('Spectrasexual', 'Spectrasexual'),
    )
    GENDER = (
        ('prefer_to_not_say', 'Prefer To Not Say'),
        ('blank_blank', '......'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Agender', 'Agender'),
        ('Androgyne', 'Androgyne'),
        ('Bigender', 'Bigender'),
        ('Butch', 'Butch'),
        ('Cisgender', 'Cisgender'),
        ('Gender Expansive', 'Gender Expansive'),
        ('Genderfluid', 'Genderfluid'),
        ('Gender Outlaw', 'Gender Outlaw'),
        ('Genderqueer', 'Genderqueer'),
        ('Masculine of Center', 'Masculine of Center'),
        ('Nonbinary', 'Nonbinary'),
        ('Omnigender', 'Omnigender'),
        ('Polygender/Pangender', 'Polygender/Pangender'),
        ('Transgender', 'Transgender'),
        ('Trans', 'Trans'),
        ('Two Spirit', 'Two Spirit'),

    )
    your_name = models.CharField(blank=True, null=True, max_length=250, default='')
    company_name = models.CharField(
        max_length=200, blank=False, null=False, default='')
    company_description = models.TextField(
        max_length=2000, blank=True, null=True, default='')
    time_employed = models.CharField(
        choices=TIME_EMPLOYED, max_length=100, blank=False, null=False, default='0_1_year')
    still_employed = models.CharField(
        choices=STILL_EMPLOYED, default='no_longer_employed', max_length=100)
    # company_location = models.CharField(max_length=300, blank=True, null=True, default='')
    # location = PlainLocationField(based_fields=['company_location'], zoom=7)
    location = LocationField()
    issues_faced = models.TextField(
        max_length=5000, blank=False, null=False, default='')
    awkwardness_rating = models.CharField(
        choices=AWKWARDNESS_RATING, max_length=10, blank=True, null=True, default='')
    sexual_orientation = models.CharField(
        choices=SEXUAL_ORIENTATION, blank=True, null=True, max_length=100, default='prefer_to_not_say')
    gender = models.CharField(choices=GENDER, blank=True,
                              null=True, max_length=100, default='prefer_to_not_say')

    class Meta:
        verbose_name_plural = 'Main Form'

    def __str__(self):
        return self.company_name
