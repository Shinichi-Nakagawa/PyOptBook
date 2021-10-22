import streamlit as st
import pandas as pd
from problem import CarGroupProblem

st.write('# 学生の乗車グループ分け問題')

students = st.file_uploader('学生データ', type='csv')
cars = st.file_uploader('車データ', type='csv')


def preprocess(dataset: dict):
    """リクエストデータを受け取り、データフレームに変換する関数"""
    # 各ファイルを取得する
    students = dataset['students']
    cars = dataset['cars']
    # pandas で読み込む
    students_df = pd.read_csv(students)
    cars_df = pd.read_csv(cars)

    return students_df, cars_df


if students and cars:
    if st.button('最適化を実行'):
        # 前処理（データ読み込み）
        students_df, cars_df = preprocess({'students': students, 'cars': cars})
        # 最適化実行
        solution_df = CarGroupProblem(students_df, cars_df).solve()
        st.write('# 最適化結果')
        st.write(solution_df)
