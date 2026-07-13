def criar_feature_engineering(df):
    df['alcohol_volatile_ratio'] = df['alcohol'] / (df['volatile acidity'] + 0.001)
    df['sulphates_alcohol_product'] = df['sulphates'] * df['alcohol']
    df['acidity_balance'] = df['citric acid'] - df['volatile acidity']
    return df