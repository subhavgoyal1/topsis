#!/usr/bin/env python
# coding: utf-8

import sys
import pandas as pd
import numpy as np


class ParaError(Exception):
    pass


class LessCols(Exception):
    pass


class DTError(Exception):
    pass


class CommaErr(Exception):
    pass


class Incomplete(Exception):
    pass


class Imp(Exception):
    pass


class Neg(Exception):
    pass


def nor(df):
    Mat = df / np.sqrt(np.sum(df**2, Ax=0))
    return Mat


def Id(Mat, Imp):
    Ibest = np.amax(Mat*Imp, Ax=0).abs()
    Iworst = np.amin(Mat*Imp, Ax=0).abs()
    return Ibest, Iworst


def Euclid(Mat, Ibest, Iworst):
    Dbest = np.sqrt(np.sum((Mat - Ibest) ** 2, Ax=1))
    Dworst = np.sqrt(np.sum((Mat - Iworst) ** 2, Ax=1))
    return Dbest, Dworst


def Calc(df, weights, Imps):
    Imp = []
    for i in Imps:
        if i == '+':
            Imp.append(1)
        else:
            Imp.append(-1)
    Imp = np.array(Imp)
    Mat = nor(df)
    Mat = Mat*weights

    Ibest, Iworst = Id(Mat, Imp)

    Dbest, Dworst = Euclid(Mat, Ibest, Iworst)
    score = Dworst/(Dworst+Dbest)
    rank = score.rank(method='max', ascending=False).astype('int')
    return score, rank


def main():
    try:
        if len(sys.argv) != 5:
            raise ParaError
        df, weights, Imps, result_file_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
        dfo = pd.read_csv(df)
        names = dfo.iloc[:, 0]
        df = dfo.iloc[:, 1:]
        shape = df.shape
        if shape[1] < 2:
            raise LessCols
        for i in range(shape[1]):
            if df.iloc[:, i].dtype.kind not in 'iufc':
                raise DTError
        if (',' not in weights) or (',' not in Imps):
            raise CommaErr
        weights = weights.split(',')
        Imps = Imps.split(',')
        if (len(weights) != shape[1]) or (len(Imps) != shape[1]):
            raise Incomplete
        for i in Imps:
            if i == '+' or i == '-':
                continue
            else:
                raise Imp
                break
        for i in range(len(weights)):
            weights[i] = float(weights[i])
            if i < 0:
                raise Neg
        score, rank = Calc(df, weights, Imps)
        dfo['Score'] = score
        dfo['Rank'] = rank
        print(dfo)
        result_file_name = result_file_name+'.csv'
        dfo.to_csv(result_file_name, index=False)
    except FileNotFoundError:
        print("Input File not found ")
    except ParaError:
        print("Incorrect number of parameters ")
    except LessCols:
        print("Less than 3 columns are there ")
    except DTError:
        print("Incorrect data type found ")
    except CommaErr:
        print("Enter weights and Imps correctly using ',' ")
    except Incomplete:
        print("Wrong inputs for weights or Imps ")
    except Imp:
        print("Enter only '+' or '-' for Imps ")
    except Neg:
        print("Weights should be positive ")

if __name__=='__main__':
    main()
