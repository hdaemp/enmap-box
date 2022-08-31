from _classic.enmapboxgeoalgorithms.provider import Help, Link

helpAlg = Help(text='Fits a PCA (Principal Component Analysis).')

helpCode = Help(text='Scikit-learn python code. See {} for information on different parameters.',
                links=[Link('http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html',
                            'PCA')
                       ])