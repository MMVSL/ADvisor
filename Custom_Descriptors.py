U
    ��ohY!  �                U   @   s  d dl Z d dlmZ d dlmZmZmZmZmZ e�	� Z
dd� Zdd� Zdd	� Zd
d� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zd d!� Zd"d#� Zd$d%� Zd&d'� Zd(d)� Zd*d+� Zd,d-� Zd.d/� Z d0d1� Z!d2d3� Z"d4d5� Z#d6d7� Z$d8d9� Z%d:d;� Z&d<d=� Z'd>d?� Z(d@dA� Z)dBdC� Z*defdefdAe)fdCe*fd	efdefdefdefdefdefdefdefdefdefdefdefd!efd#efd%efd'efd)efd+efd-efd/e fd1e!fd3e"fd5e#fd7e$fd9e%fd;e&fd=e'fgZ+defd!efd#efd%efd'efd)efd+efd-efd/e fd;e&fd=e'fgZ,dd!d#d%d'd)d+d-d/d;d=gZ-dDdEdFdGdHdIdJdKdLdMdNdOdPdQdRdSdTdUdVdWdXdYdZd[d\d]d^d_d`dadbdcdddedfdgdhdidjdkdldmdndodpdqdrdsdtdudvdwdxdydzd{d|d}d~dd�d�d�d�d�d�d�d�d�d�d�d�d�d�d�d�d�d�d�d�d�d�d�d�d�gUZ.dS )��    N)�Chem)�	Fragments�rdMolDescriptors�AllChem�Descriptors�DataStructsc                 C   s   t j�t �| ��S )zmolecular weight)r   r   �
ExactMolWt�AddHs��mol� r   �Custom_Descriptors.py�MW   s    r   c                 C   s$   t j�t �| ��t j�t �| �� S )zaverage molecular weight)r   r   r   r	   r   �CalcNumAtomsr
   r   r   r   �AMW   s    r   c                 C   s   t j�t �| ��S )znumber of atoms)r   r   r   r	   r
   r   r   r   �nAt   s    r   c                 C   s   t j�t �| ��S )znumber of heavy atoms)r   r   ZCalcNumHeavyAtomsr	   r
   r   r   r   �nSk   s    r   c                 C   s   t �| ��� S )ztotal number of bonds)r   r	   �GetNumBondsr
   r   r   r   �nBt   s    r   c                 C   s   t �| ��� S )znumber of non H bonds)r   ZRemoveHsr   r
   r   r   r   �nBo   s    r   c                 C   s   t dd� | �� D ��S )znumber of multiple bondsc                 S   s   g | ]}|� � d krd �qS ��   ��GetBondTypeAsDouble��.0�bondr   r   r   �
<listcomp>   s      znBm.<locals>.<listcomp>��sum�GetBondsr
   r   r   r   �nBm   s    r!   c                 C   s   t dd� | �� D ��S )znumber of double bondsc                 S   s   g | ]}|� � d krd�qS )�   r   r   r   r   r   r   r   "   s      znDblBo.<locals>.<listcomp>r   r
   r   r   r   �nDblBo    s    r#   c                 C   s   t dd� | �� D ��S )znumber of triple bondsc                 S   s   g | ]}|� � d krd�qS )�   r   r   r   r   r   r   r   %   s      znTrpBo.<locals>.<listcomp>r   r
   r   r   r   �nTrpBo#   s    r%   c                 C   s   t dd� | �� D ��S )znumber of aromatic bondsc                 S   s   g | ]}|� � d krd�qS )g      �?r   r   r   r   r   r   r   (   s      znArBo.<locals>.<listcomp>r   r
   r   r   r   �nArBo&   s    r&   c                 C   sB   d}| � � D ]0}|�� �� dkr|�� �� dkr||�� 7 }q|S )zZsum of conventional bond order, defined as the sum of bond orders of bonds not involving Hr   r   )r    ZGetBeginAtomZGetAtomicNumZ
GetEndAtomr   )r   Zscbor   r   r   r   �SCBO)   s
     r'   c                 C   s   t dd� t�| ��� D ��S )znumber of H atomsc                 S   s   g | ]}|� � d krd�qS ��Hr   ��	GetSymbol�r   �atomr   r   r   r   2   s      znH.<locals>.<listcomp>�r   r   r	   �GetAtomsr
   r   r   r   �nH0   s    r0   c                 C   s   t dd� t�| ��� D ��S )znumber of C atomsc                 S   s   g | ]}|� � d krd�qS ��Cr   r*   r,   r   r   r   r   5   s      znC.<locals>.<listcomp>r.   r
   r   r   r   �nC3   s    r3   c                 C   s   t dd� t�| ��� D ��S )znumber of N atomsc                 S   s   g | ]}|� � d krd�qS ��Nr   r*   r,   r   r   r   r   8   s      znN.<locals>.<listcomp>r.   r
   r   r   r   �nN6   s    r6   c                 C   s   t dd� t�| ��� D ��S )znumber of O atomsc                 S   s   g | ]}|� � d krd�qS ��Or   r*   r,   r   r   r   r   ;   s      znO.<locals>.<listcomp>r.   r
   r   r   r   �nO9   s    r9   c                 C   s   t dd� t�| ��� D ��S )znumber of P atomsc                 S   s   g | ]}|� � d krd�qS )�Pr   r*   r,   r   r   r   r   >   s      znP.<locals>.<listcomp>r.   r
   r   r   r   �nP<   s    r;   c                 C   s   t dd� t�| ��� D ��S )znumber of S atomsc                 S   s   g | ]}|� � d krd�qS )�Sr   r*   r,   r   r   r   r   A   s      znS.<locals>.<listcomp>r.   r
   r   r   r   �nS?   s    r=   c                 C   s   t dd� t�| ��� D ��S )znumber of F atomsc                 S   s   g | ]}|� � d krd�qS )�Fr   r*   r,   r   r   r   r   D   s      znF.<locals>.<listcomp>r.   r
   r   r   r   �nFB   s    r?   c                 C   s   t dd� t�| ��� D ��S )znumber of Cl atomsc                 S   s   g | ]}|� � d krd�qS )�Clr   r*   r,   r   r   r   r   G   s      znCl.<locals>.<listcomp>r.   r
   r   r   r   �nClE   s    rA   c                 C   s   t dd� t�| ��� D ��S )znumber of Br atomsc                 S   s   g | ]}|� � d krd�qS )�Brr   r*   r,   r   r   r   r   J   s      znBr.<locals>.<listcomp>r.   r
   r   r   r   �nBrH   s    rC   c                 C   s   t dd� t�| ��� D ��S )znumber of I atomsc                 S   s   g | ]}|� � d krd�qS )�Ir   r*   r,   r   r   r   r   M   s      znI.<locals>.<listcomp>r.   r
   r   r   r   �nIK   s    rE   c                 C   s   t dd� t�| ��� D ��S )znumber of B atomsc                 S   s   g | ]}|� � d krd�qS )�Br   r*   r,   r   r   r   r   P   s      znB.<locals>.<listcomp>r.   r
   r   r   r   �nBN   s    rG   c                 C   s.   t dd� t�| ��� D ��tj�t�| �� S )z4percentage of H atoms over the total number of atomsc                 S   s   g | ]}|� � d krd�qS r(   r*   r,   r   r   r   r   S   s      zHPerc.<locals>.<listcomp>�r   r   r	   r/   r   r   r
   r   r   r   �HPercQ   s    rI   c                 C   s.   t dd� t�| ��� D ��tj�t�| �� S )z4percentage of C atoms over the total number of atomsc                 S   s   g | ]}|� � d krd�qS r1   r*   r,   r   r   r   r   V   s      zCPerc.<locals>.<listcomp>rH   r
   r   r   r   �CPercT   s    rJ   c                 C   s.   t dd� t�| ��� D ��tj�t�| �� S )z4percentage of N atoms over the total number of atomsc                 S   s   g | ]}|� � d krd�qS r4   r*   r,   r   r   r   r   Y   s      zNPerc.<locals>.<listcomp>rH   r
   r   r   r   �NPercW   s    rK   c                 C   s.   t dd� t�| ��� D ��tj�t�| �� S )z4percentage of O atoms over the total number of atomsc                 S   s   g | ]}|� � d krd�qS r7   r*   r,   r   r   r   r   \   s      zOPerc.<locals>.<listcomp>rH   r
   r   r   r   �OPercZ   s    rL   c                 C   s.   t dd� t�| ��� D ��tj�t�| �� S )z;percentage of halogens atoms over the total number of atomsc                 S   s   g | ]}|� � d krd�qS �)r@   r>   rB   rD   r   r*   r,   r   r   r   r   _   s      zXPerc.<locals>.<listcomp>rH   r
   r   r   r   �XPerc]   s    rN   c                 C   s   t j�t �| ��S )znumber of heteroatoms)r   r   ZCalcNumHeteroatomsr	   r
   r   r   r   �nHet`   s    rO   c                 C   s   t dd� t�| ��� D ��S )znumber of halogensc                 S   s   g | ]}|� � d krd�qS rM   r*   r,   r   r   r   r   e   s      znX.<locals>.<listcomp>r.   r
   r   r   r   �nXc   s    rP   c                 C   s   dt j | d  S )z0calculate the volum of a sphere given its radiusgUUUUUU�?r$   )�mathZpi)�rr   r   r   �_sphere_volumef   s    rS   c                 C   sD   d}t �| ��� D ],}tt�|�� ��tt�d�� }||7 }q|S )z�sum of atomic van der waals volumes (scaled on carbon atom). Not exactly the same results as Padel's, but close.
    Might be nice to evaluate the use of radi by Bondir   r2   )r   r	   r/   rS   �pt�GetRvdwr+   �r   �svr-   Zvolr   r   r   �Svi   s
     
rX   c                 C   s`   d}t �| ��� D ],}tt�|�� ��tt�d�� }||7 }q|tdd� t �| ��� D �� S )z�mean of atomic van der waals volumes (scaled on carbon atom). Not exactly the same results as Padel's, but close.
    Might be nice to evaluate the use of radi by Bondir   r2   c                 S   s   g | ]}d �qS r   r   )r   �xr   r   r   r   x   s     zMv.<locals>.<listcomp>)r   r	   r/   rS   rT   rU   r+   r   rV   r   r   r   �Mvq   s
     
rZ   Z	fr_Al_COOZfr_Al_OHZfr_Al_OH_noTertZfr_ArNZ	fr_Ar_COOZfr_Ar_NZfr_Ar_NHZfr_Ar_OHZfr_COOZfr_COO2Zfr_C_OZfr_C_O_noCOOZfr_C_SZfr_HOCCNZfr_ImineZfr_NH0Zfr_NH1Zfr_NH2Zfr_N_OZfr_Ndealkylation1Zfr_Ndealkylation2Zfr_NhpyrroleZfr_SHZfr_aldehydeZfr_alkyl_carbamateZfr_alkyl_halideZfr_allylic_oxidZfr_amideZ
fr_amidineZ
fr_anilineZfr_aryl_methylZfr_azideZfr_azoZfr_barbiturZ
fr_benzeneZfr_benzodiazepineZfr_bicyclicZfr_diazoZfr_dihydropyridineZ
fr_epoxideZfr_esterZfr_etherZfr_furanZ
fr_guanidoZ
fr_halogenZ
fr_hdrzineZ
fr_hdrzoneZfr_imidazoleZfr_imideZ
fr_isocyanZfr_isothiocyanZ	fr_ketoneZfr_ketone_ToplissZ	fr_lactamZ
fr_lactoneZ
fr_methoxyZfr_morpholineZ
fr_nitrileZfr_nitroZfr_nitro_aromZfr_nitro_arom_nonorthoZ
fr_nitrosoZ
fr_oxazoleZfr_oximeZfr_para_hydroxylationZ	fr_phenolZfr_phenol_noOrthoHbondZfr_phos_acidZfr_phos_esterZfr_piperdineZfr_piperzineZfr_priamideZfr_prisulfonamdZfr_pyridineZfr_quatNZ
fr_sulfideZfr_sulfonamdZ
fr_sulfoneZfr_term_acetyleneZfr_tetrazoleZfr_thiazoleZfr_thiocyanZfr_thiopheneZfr_unbrch_alkaneZfr_urea)/rQ   Zrdkitr   Z
rdkit.Chemr   r   r   r   r   ZGetPeriodicTablerT   r   r   r   r   r   r   r!   r#   r%   r&   r'   r0   r3   r6   r9   r;   r=   r?   rA   rC   rE   rG   rI   rJ   rK   rL   rN   rO   rP   rS   rX   rZ   Zconstitutional_desc_listZheteroatoms_desc_list_tuplesZheteroatoms_desc_listZfunctional_groups_namesr   r   r   r   �<module>   sb  
�!���