import pandas as pd

def perform_analysis(df, main_feature, selected_features, top_n=5):
    """Performs the analysis based on selected features"""
    try:
        result = df[[main_feature] + selected_features].sort_values(by=selected_features, ascending=False).head(top_n)
        return result
    except KeyError as e:
       raise KeyError(f"Selected column '{e}' not found in dataframe columns")
    except Exception as e:
        raise Exception(f"An error occurred during analysis: {e}")

def perform_aggregation(df, main_feature, selected_features, top_n, agg_type):
  try:
     if agg_type in ["mean","median","sum"]:
        agg_df = df.groupby(selected_features)[main_feature].agg(agg_type).reset_index()
        agg_df = agg_df.sort_values(by=main_feature, ascending=False).head(top_n)
        return agg_df
     else:
        raise ValueError("Invalid aggregation type.")
  except KeyError as e:
     raise KeyError(f"Selected column '{e}' not found in dataframe columns")
  except Exception as e:
        raise Exception(f"An error occurred during aggregation: {e}")