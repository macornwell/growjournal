# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0001_initial'),
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseEvent',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('purchase_record_id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('count', models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)),
                ('price_currency', djmoney.models.fields.CurrencyField(choices=[('AFN', 'Afghani'), ('DZD', 'Algerian Dinar'), ('ARS', 'Argentine Peso'), ('AMD', 'Armenian Dram'), ('AWG', 'Aruban Guilder'), ('AUD', 'Australian Dollar'), ('AZN', 'Azerbaijanian Manat'), ('BSD', 'Bahamian Dollar'), ('BHD', 'Bahraini Dinar'), ('THB', 'Baht'), ('BBD', 'Barbados Dollar'), ('BYR', 'Belarussian Ruble'), ('BZD', 'Belize Dollar'), ('BMD', 'Bermudian Dollar (customarily known as Bermuda Dollar)'), ('BTN', 'Bhutanese ngultrum'), ('VEF', 'Bolivar Fuerte'), ('XBA', 'Bond Markets Units European Composite Unit (EURCO)'), ('BRL', 'Brazilian Real'), ('BND', 'Brunei Dollar'), ('BGN', 'Bulgarian Lev'), ('BIF', 'Burundi Franc'), ('XOF', 'CFA Franc BCEAO'), ('XAF', 'CFA franc BEAC'), ('XPF', 'CFP Franc'), ('CAD', 'Canadian Dollar'), ('CVE', 'Cape Verde Escudo'), ('KYD', 'Cayman Islands Dollar'), ('CLP', 'Chilean peso'), ('XTS', 'Codes specifically reserved for testing purposes'), ('COP', 'Colombian peso'), ('KMF', 'Comoro Franc'), ('CDF', 'Congolese franc'), ('BAM', 'Convertible Marks'), ('NIO', 'Cordoba Oro'), ('CRC', 'Costa Rican Colon'), ('HRK', 'Croatian Kuna'), ('CUP', 'Cuban Peso'), ('CUC', 'Cuban convertible peso'), ('CZK', 'Czech Koruna'), ('GMD', 'Dalasi'), ('DKK', 'Danish Krone'), ('MKD', 'Denar'), ('DJF', 'Djibouti Franc'), ('STD', 'Dobra'), ('DOP', 'Dominican Peso'), ('VND', 'Dong'), ('XCD', 'East Caribbean Dollar'), ('EGP', 'Egyptian Pound'), ('ETB', 'Ethiopian Birr'), ('EUR', 'Euro'), ('XBB', 'European Monetary Unit (E.M.U.-6)'), ('XBD', 'European Unit of Account 17(E.U.A.-17)'), ('XBC', 'European Unit of Account 9(E.U.A.-9)'), ('FKP', 'Falkland Islands Pound'), ('FJD', 'Fiji Dollar'), ('HUF', 'Forint'), ('GHS', 'Ghana Cedi'), ('GIP', 'Gibraltar Pound'), ('XAU', 'Gold'), ('XFO', 'Gold-Franc'), ('PYG', 'Guarani'), ('GNF', 'Guinea Franc'), ('GYD', 'Guyana Dollar'), ('HTG', 'Haitian gourde'), ('HKD', 'Hong Kong Dollar'), ('UAH', 'Hryvnia'), ('ISK', 'Iceland Krona'), ('INR', 'Indian Rupee'), ('IRR', 'Iranian Rial'), ('IQD', 'Iraqi Dinar'), ('IMP', 'Isle of Man pount'), ('JMD', 'Jamaican Dollar'), ('JOD', 'Jordanian Dinar'), ('KES', 'Kenyan Shilling'), ('PGK', 'Kina'), ('LAK', 'Kip'), ('KWD', 'Kuwaiti Dinar'), ('AOA', 'Kwanza'), ('MMK', 'Kyat'), ('GEL', 'Lari'), ('LVL', 'Latvian Lats'), ('LBP', 'Lebanese Pound'), ('ALL', 'Lek'), ('HNL', 'Lempira'), ('SLL', 'Leone'), ('LSL', 'Lesotho loti'), ('LRD', 'Liberian Dollar'), ('LYD', 'Libyan Dinar'), ('SZL', 'Lilangeni'), ('LTL', 'Lithuanian Litas'), ('MGA', 'Malagasy Ariary'), ('MWK', 'Malawian Kwacha'), ('MYR', 'Malaysian Ringgit'), ('TMM', 'Manat'), ('MUR', 'Mauritius Rupee'), ('MZN', 'Metical'), ('MXN', 'Mexican peso'), ('MDL', 'Moldovan Leu'), ('MAD', 'Moroccan Dirham'), ('NGN', 'Naira'), ('ERN', 'Nakfa'), ('NAD', 'Namibian Dollar'), ('NPR', 'Nepalese Rupee'), ('ANG', 'Netherlands Antillian Guilder'), ('ILS', 'New Israeli Sheqel'), ('RON', 'New Leu'), ('TWD', 'New Taiwan Dollar'), ('NZD', 'New Zealand Dollar'), ('KPW', 'North Korean Won'), ('NOK', 'Norwegian Krone'), ('PEN', 'Nuevo Sol'), ('MRO', 'Ouguiya'), ('TOP', 'Paanga'), ('PKR', 'Pakistan Rupee'), ('XPD', 'Palladium'), ('MOP', 'Pataca'), ('PHP', 'Philippine Peso'), ('XPT', 'Platinum'), ('GBP', 'Pound Sterling'), ('BWP', 'Pula'), ('QAR', 'Qatari Rial'), ('GTQ', 'Quetzal'), ('ZAR', 'Rand'), ('OMR', 'Rial Omani'), ('KHR', 'Riel'), ('MVR', 'Rufiyaa'), ('IDR', 'Rupiah'), ('RUB', 'Russian Ruble'), ('RWF', 'Rwanda Franc'), ('XDR', 'SDR'), ('SHP', 'Saint Helena Pound'), ('SAR', 'Saudi Riyal'), ('RSD', 'Serbian Dinar'), ('SCR', 'Seychelles Rupee'), ('XAG', 'Silver'), ('SGD', 'Singapore Dollar'), ('SBD', 'Solomon Islands Dollar'), ('KGS', 'Som'), ('SOS', 'Somali Shilling'), ('TJS', 'Somoni'), ('LKR', 'Sri Lanka Rupee'), ('SDG', 'Sudanese Pound'), ('SRD', 'Surinam Dollar'), ('SEK', 'Swedish Krona'), ('CHF', 'Swiss Franc'), ('SYP', 'Syrian Pound'), ('BDT', 'Taka'), ('WST', 'Tala'), ('TZS', 'Tanzanian Shilling'), ('KZT', 'Tenge'), ('TTD', 'Trinidad and Tobago Dollar'), ('MNT', 'Tugrik'), ('TND', 'Tunisian Dinar'), ('TRY', 'Turkish Lira'), ('TVD', 'Tuvalu dollar'), ('AED', 'UAE Dirham'), ('XFU', 'UIC-Franc'), ('USD', 'US Dollar'), ('UGX', 'Uganda Shilling'), ('UYU', 'Uruguayan peso'), ('UZS', 'Uzbekistan Sum'), ('VUV', 'Vatu'), ('KRW', 'Won'), ('YER', 'Yemeni Rial'), ('JPY', 'Yen'), ('CNY', 'Yuan Renminbi'), ('ZMK', 'Zambian Kwacha'), ('ZMW', 'Zambian Kwacha'), ('ZWD', 'Zimbabwe Dollar A/06'), ('ZWN', 'Zimbabwe dollar A/08'), ('ZWL', 'Zimbabwe dollar A/09'), ('PLN', 'Zloty')], max_length=3, default='USD', editable=False)),
                ('price', djmoney.models.fields.MoneyField(decimal_places=2, max_digits=10, default_currency='USD', default=None, null=True, blank=True)),
                ('life_form', models.ForeignKey(to='taxonomy.LifeForm')),
                ('project', models.ForeignKey(null=True, to='core.Project', blank=True)),
                ('site', models.ForeignKey(to='core.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('store_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('url', models.URLField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='purchaseevent',
            name='store',
            field=models.ForeignKey(null=True, to='purchase.Store', blank=True),
        ),
        migrations.AddField(
            model_name='purchaseevent',
            name='unit',
            field=models.ForeignKey(null=True, to='core.Unit', blank=True),
        ),
        migrations.AddField(
            model_name='purchaseevent',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
