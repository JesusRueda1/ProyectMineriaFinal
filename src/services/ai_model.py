import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def train_linear_model(df, target, feats):
    """Entrena modelo y devuelve artefactos."""
    try:
        df_c = df.dropna(subset=feats+[target])
        X = df_c[feats]
        y = df_c[target]
        
        pre = ColumnTransformer([
            ('num', StandardScaler(), X.select_dtypes(include=['number']).columns),
            ('cat', OneHotEncoder(handle_unknown='ignore'), X.select_dtypes(exclude=['number']).columns)
        ])
        
        model = Pipeline([('pre', pre), ('reg', LinearRegression())])
        
        X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
        model.fit(X_tr, y_tr)
        
        y_p = model.predict(X_te)
        metrics = {
            "r2": r2_score(y_te, y_p),
            "mse": mean_squared_error(y_te, y_p)
        }
        
        return model, metrics
    except Exception as e:
        raise e