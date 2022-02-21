import pandas as pd
class DataFrame():
    def init(self,df):
        self._nombre = df
        self._df = pd.read_json('./'+("pokemones")+'.json')
    @property
    def df(self):
        return self._df

    def exportar(self):
        self._df.to_json('./'+"pokemones"+'.json')

    def actualizar(self, fila, columna, datoAct):
        self._df.loc[fila, [columna][0]]=[datoAct]

