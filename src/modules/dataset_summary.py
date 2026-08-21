"""Funções para analisar e resumir um DataFrame sem modificá-lo."""

# Importa o pandas, biblioteca usada pelo projeto para trabalhar com DataFrames.
import pandas as pd

# Importa funções específicas para identificar os tipos das colunas de forma segura.
from pandas.api.types import (
    is_bool_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
    is_string_dtype,
    is_timedelta64_dtype,
)


def detect_column_type(column: pd.Series) -> str:
    """Converte o tipo técnico do pandas em um tipo lógico mais amigável."""

    # Verifica booleanos antes de números, pois booleanos podem ser tratados como 0 e 1.
    if is_bool_dtype(column.dtype):
        return "boolean"

    # Verifica se a coluna já possui um tipo de data reconhecido pelo pandas.
    if is_datetime64_any_dtype(column.dtype):
        return "datetime"

    # Identifica durações, como diferenças entre datas ou tempos decorridos.
    if is_timedelta64_dtype(column.dtype):
        return "timedelta"

    # Agrupa inteiros e números decimais no tipo lógico "number".
    if is_numeric_dtype(column.dtype):
        return "number"

    # Identifica colunas categóricas criadas explicitamente com o tipo category.
    if isinstance(column.dtype, pd.CategoricalDtype):
        return "category"

    # Considera strings e objetos como texto nesta primeira versão da detecção.
    if is_string_dtype(column.dtype) or is_object_dtype(column.dtype):
        return "text"

    # Usa "other" quando o pandas possuir um tipo não coberto pelas regras anteriores.
    return "other"


def summarize_dataset(dataframe: pd.DataFrame) -> dict:
    """Retorna métricas gerais e detalhes de cada coluna de um DataFrame."""

    # Garante que a função recebeu realmente um DataFrame antes de iniciar a análise.
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("dataframe deve ser uma instância de pandas.DataFrame")

    # Cria um dicionário para armazenar quantas colunas existem de cada tipo lógico.
    type_counts: dict[str, int] = {}

    # Cria outro dicionário para armazenar as informações individuais das colunas.
    column_details: dict[str, dict] = {}

    # Percorre o nome e os valores de cada coluna do DataFrame.
    for column_name, column in dataframe.items():
        # Detecta um tipo lógico mais fácil de apresentar na interface da aplicação.
        logical_type = detect_column_type(column)

        # Incrementa a contagem do tipo atual ou inicia essa contagem em 1.
        type_counts[logical_type] = type_counts.get(logical_type, 0) + 1

        # Conta quantas células vazias existem especificamente nesta coluna.
        missing_values = int(column.isna().sum())

        # Calcula a porcentagem de células vazias e evita divisão por zero em datasets vazios.
        missing_percentage = (
            round((missing_values / len(dataframe)) * 100, 2)
            if len(dataframe) > 0
            else 0.0
        )

        # Conta valores diferentes sem incluir valores ausentes nessa quantidade.
        unique_values = int(column.nunique(dropna=True))

        # Guarda os resultados desta coluna usando tipos simples, fáceis de exibir ou serializar.
        column_details[str(column_name)] = {
            "pandas_type": str(column.dtype),
            "detected_type": logical_type,
            "missing_values": missing_values,
            "missing_percentage": missing_percentage,
            "unique_values": unique_values,
        }

    # Obtém separadamente o número de linhas e de colunas por meio do atributo shape.
    row_count, column_count = dataframe.shape

    # Soma todas as células ausentes presentes no dataset inteiro.
    total_missing_values = int(dataframe.isna().sum().sum())

    # Calcula o número total de células para permitir o cálculo percentual de ausências.
    total_cells = int(row_count * column_count)

    # Calcula a porcentagem geral de valores ausentes, protegendo datasets sem células.
    total_missing_percentage = (
        round((total_missing_values / total_cells) * 100, 2)
        if total_cells > 0
        else 0.0
    )

    # Conta linhas completamente duplicadas; a primeira ocorrência não é considerada duplicada.
    duplicate_rows = int(dataframe.duplicated().sum())

    # Soma a memória usada pelas colunas e pelo índice, retornando o valor em bytes.
    memory_usage_bytes = int(dataframe.memory_usage(index=True, deep=True).sum())

    # Organiza as métricas gerais em um dicionário separado dos detalhes por coluna.
    general_summary = {
        "rows": int(row_count),
        "columns": int(column_count),
        "total_cells": total_cells,
        "missing_values": total_missing_values,
        "missing_percentage": total_missing_percentage,
        "duplicate_rows": duplicate_rows,
        "memory_usage_bytes": memory_usage_bytes,
        "type_counts": type_counts,
    }

    # Retorna uma única estrutura contendo o resumo geral e a análise individual das colunas.
    return {
        "summary": general_summary,
        "columns": column_details,
    }
