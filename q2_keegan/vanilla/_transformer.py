import pandas as pd

from . import VanillaBeanFmt
from ..plugin_setup import plugin


@plugin.register_transformer
def _vanilla_bean_to_py_list(ff: VanillaBeanFmt) -> list:
    with ff.open() as fh:
        return [i.strip('\n') for i in fh.readlines()]


@plugin.register_transformer
def _py_list_to_vanilla_bean(in_list: list) ->  VanillaBeanFmt:

    ff = VanillaBeanFmt()

    with ff.open() as fh:
        for item in in_list:
            fh.write(str(item.rstrip('\n') + '\n'))

    return ff

def _vanilla_bean_to_df(ff: VanillaBeanFmt) -> pd.DataFrame:
    with ff.open() as fw:
        return pd.read_csv(fw, sep="\t")
    #vb_df = pd.DataFrame()
    #return vb_df.read_csv(ff, sep="\t")

def _df_to_vanilla_bean(df):
    ff = VanillaBeanFmt()

    with ff.open() as fh:
        df.to_csv(fh, sep="\t")

    return ff

@plugin.register_transformer
def _1(data: pd.DataFrame) -> VanillaBeanFmt:
    return _df_to_vanilla_bean(data)

@plugin.register_transformer
def _2(data: VanillaBeanFmt) -> pd.DataFrame:
    return _vanilla_bean_to_df(data)
#
#    ff = VanillaBeanFmt()
#
#    with ff.open() as fh:
#        data.to_csv(fw, sep="\t")
#
#    return ff
