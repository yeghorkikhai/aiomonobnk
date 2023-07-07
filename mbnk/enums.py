from enum import Enum


class PaymentType(str, Enum):
    debit = "debit"
    hold = "hold"


class PaymentScheme(str, Enum):
    full = "full"
    bnpl_parts_4 = "bnpl_parts_4"
    bnpl_later_30 = "bnpl_later_30"


class PaymentMethod(str, Enum):
    pan = "pan"
    apple = "apple"
    google = "google"
    monobank = "monobank"


class AmountType(str, Enum):
    merchant = "merchant"
    client = "client"
    fix = "fix"


class TransactionStatus(str, Enum):
    created = "created"
    processing = "processing"
    hold = "hold"
    success = "success"
    failure = "failure"
    reversed = "reversed"
    expired = "expired"


class CancellationStatus(str, Enum):
    processing = "processing"
    success = "success"
    failure = "failure"


class TokenizedCardStatus(str, Enum):
    new = "new"
    created = "created"
    failed = "failed"


class AccountType(str, Enum):
    black = "black"
    white = "white"
    platinum = "platinum"
    iron = "iron"
    fop = "fop"
    yellow = "yellow"
    eAid = "eAid"


class CashbackType(str, Enum):
    NONE = "None"
    UAH = "UAH"
    MILES = "Miles"


class RegistrationStatus(str, Enum):
    new = "New"
    declined = "Declined"
    approved = "Approved"


class CurrencyCode(int, Enum):
    UAH = 980
    USD = 840
    EUR = 978
    GBP = 826
    JPY = 392
    CHF = 756
    CNY = 156
    AED = 784
    AFN = 971
    ALL = 8
    AMD = 51
    AOA = 973
    ARS = 32
    AUD = 36
    AZN = 944
    BDT = 50
    BGN = 975
    BHD = 48
    BIF = 108
    BND = 96
    BOB = 68
    BRL = 986
    BWP = 72
    BYN = 933
    CAD = 124
    CDF = 976
    CLP = 152
    COP = 170
    CRC = 188
    CUP = 192
    CZK = 203
    DJF = 262
    DKK = 208
    DZD = 12
    EGP = 818
    ETB = 230
    GEL = 981
    GHS = 936
    GMD = 270
    GNF = 324
    HKD = 344
    HRK = 191
    HUF = 348
    IDR = 360
    ILS = 376
    INR = 356
    IQD = 368
    IRR = 364
    ISK = 352
    JOD = 400
    KES = 404
    KGS = 417
    KHR = 116
    KPW = 408
    KRW = 410
    KWD = 414
    KZT = 398
    LAK = 418
    LBP = 422
    LKR = 144
    LYD = 434
    MAD = 504
    MDL = 498
    MGA = 969
    MKD = 807
    MNT = 496
    MRO = 478
    MUR = 480
    MVR = 462
    MWK = 454
    MXN = 484
    MYR = 458
    MZN = 943
    NAD = 516
    NGN = 566
    NIO = 558
    NOK = 578
    NPR = 524
    NZD = 554
    OMR = 512
    PEN = 604
    PHP = 608
    PKR = 586
    PLN = 985
    PYG = 600
    QAR = 634
    RON = 946
    RSD = 941
    SAR = 682
    SCR = 690
    SDG = 938
    SEK = 752
    SGD = 702
    SLL = 694
    SOS = 706
    SRD = 968
    SYP = 760
    SZL = 748
    THB = 764
    TJS = 972
    TMT = 795
    TND = 788
    TRY = 949
    TWD = 901
    TZS = 834
    UGZ = 800
    UYU = 858
    UZS = 860
    VEF = 937
    VND = 704
    XAF = 950
    XDR = 960
    XOF = 952
    YER = 886
    ZAR = 710
    ZMK = 894