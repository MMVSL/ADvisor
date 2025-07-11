U
    �oh#  �                   @   s�   d dl Zd dlmZ d dlZd dlZd dlZdZej	�
de�Zej�eje�Zej�e�Ze�e� eejd< d dlmZ ddd	�Zddd�Zddd�Zddd�ZdS )�    N)�ChemzMACCS_smarts.py�MACCS_smarts)�smartsPatts�Similarity_Rank_VS_Train�   c           	         s�   |dkrt d� d S g }| �� D ]`\}}|| d |� � � fdd�t|�D �}|d |d  }t|�| d|d   }|�|� q |S )Nr   �`[WARNING] Implemented to consider 2 most similar neighbors. Changes in the code may be required.c                    s   g | ]}� | d  �qS �r   � ��.0Zk_iter�Z
top_tuplesr	   �AD_Indexes.py�
<listcomp>   s     z$similarity_index.<locals>.<listcomp>r   �   )�print�iterrows�range�sum�append)	�df�storage_col�kZSI_s�i�row�SkZDiamZSIr	   r   r   �similarity_index   s    r   �Similarity_Rank_VS_Test�Predicted_Value�
True_Value�	regressorc                    s�  |dkr�|dkrt d� d S g }| �� D ]�\}}	|	| d |� � � fdd�t|�D �}
� fdd�t|�D �}g }t|�D ]2\}}| j| | | j| | krx|�|
| � qxtt�dt�	|� ��}tt�dt�	|
� ��}|�|| � q(|S |dk�r�|dk�rt d� d S g }| �� D ]�\}}	|	| d |� � � fd	d�t|�D �}
� fd
d�t|�D �}g }t|�D ]>\}}t
| j| | | j| |  �|k�rl|�|
| � �qltt�dt�	|� ��}tt�dt�	|
� ��}|�|| � �q|S td��d S )N�
classifierr   r   c                    s   g | ]}� | d  �qS r   r	   r
   r   r	   r   r   (   s     z"accuracy_index.<locals>.<listcomp>c                    s   g | ]}� | d  �qS �r   r	   r
   r   r	   r   r   )   s     r   r   c                    s   g | ]}� | d  �qS r   r	   r
   r   r	   r   r   9   s     c                    s   g | ]}� | d  �qS r!   r	   r
   r   r	   r   r   :   s     �5Wrong model_type. Options are [classifier, regressor]�r   r   r   �	enumerateZilocr   r   �npZlog10Zarray�abs�
ValueError)r   r   �test_prediction_colZtest_true_value_col�
model_typer   �tollerated_error_rangeZAI_sr   r   r   �Sk_index�Sc�index�	numerator�denominatorr	   r   r   �accuracy_index    sF    

&r0   c                    s�  |dkr�|dkrt d� d S g }| �� D ]�\}	}
|
| d |� � � fdd�t|�D �}� fdd�t|�D �}g }t|�D ],\}	}|j| | |
| krx|�||	 � qxtt�dt�	|� ��}tt�dt�	|� ��}|�|| � q(|S |dk�r�|dk�r
t d� d S g }| �� D ]�\}	}
|
| d |� � � fd	d�t|�D �}� fd
d�t|�D �}g }t|�D ]8\}	}t
|j| | |
|  �|k�rf|�||	 � �qftt�dt�	|� ��}tt�dt�	|� ��}|�|| � �q|S td��d S )Nr    r   r   c                    s   g | ]}� | d  �qS r   r	   r
   r   r	   r   r   N   s     z%concordance_index.<locals>.<listcomp>c                    s   g | ]}� | d  �qS r!   r	   r
   r   r	   r   r   O   s     r   r   c                    s   g | ]}� | d  �qS r   r	   r
   r   r	   r   r   _   s     c                    s   g | ]}� | d  �qS r!   r	   r
   r   r	   r   r   `   s     r"   r#   )�test�trainr   r(   Ztrain_true_value_colr)   r   r*   ZCI_sr   r   r   r+   r,   r-   r.   r/   r	   r   r   �concordance_indexF   sF    

 r3   �SMILESc                 C   s�  dd� || � � D �}i }t�� D ]�\}}|d }t�|�}	|	d k	r"d}
|D ]*}|�|	�rL|
d7 }
|
dkrLd||<  q"qLd|
  k r�dkr�n n
d||< q"|
dkr"d	||< q"g }| | � � D ]�}i }t�|�}d
\}}|�� D ]0\}}t�|�}	|�|	��rd||< q�d||< q�|�� D ]D\}}|dk�r|�|�dk�rB|d7 }|�|�d	k�r|d7 }�q|dk�rnd}n|dk�r~d}nd}|dk�r�d}n|dk�r�d}nd}|�|| � q�|S )Nc                 S   s   g | ]}t �|��qS r	   )r   �MolFromSmiles)r   �smir	   r	   r   r   n   s     z/fragment_contribution_index.<locals>.<listcomp>r   r   �   �commonr   �rare�missing)r   r   ZpresentZabsentg      �?g333333�?g�������?)	�tolistr   �itemsr   ZMolFromSmartsZHasSubstructMatchr5   �getr   )r1   r2   Ztest_smi_colZtrain_smi_colZ
train_molsZtrain_fragments_dictr   �valueZsmartsZqueryZcounter_occurrencesZmolZFC_indexr6   Zmolecule_fragmentsZ
rare_countZmissing_countZtrain_labelZ	frag_nameZis_present_in_test_molr9   r:   r	   r	   r   �fragment_contribution_indexm   sZ    












r?   )r   r   )r   r   r   r   r   N)r   r   r   r   r   N)r4   r4   )Znumpyr%   Zrdkitr   Zimportlib.machinery�	importlib�importlib.util�sysZpy_path�	machinery�SourcelessFileLoader�loader�util�spec_from_loader�name�spec�module_from_specr   �exec_module�modulesr   r   r0   r3   r?   r	   r	   r	   r   �<module>   s   



&
'