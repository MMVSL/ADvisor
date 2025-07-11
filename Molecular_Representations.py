U
    !�oh�,  �                   @   sF  d dl Zd dlZd dlmZ d dlmZmZmZm	Z	m
Z
 d dlmZ d dlZd dlZe�d�Zd dlZd dlZd dlZdZej�de�Zej�eje�Zej�e�Ze�e� eejd< d dlT d	Zej�d
e�Zej�eje�Zej�e�Z e�e � e ejd
< d dl Z G dd� d�Z!G dd� d�Z"G dd� d�Z#G dd� d�Z$dS )�    N)�Chem)�	Fragments�rdMolDescriptors�AllChem�Descriptors�DataStructs)�tqdmzrdkit_208-desc_list.dumpzCustom_Descriptors.py�Custom_Descriptors)�*zPubChemFingerprints.py�PubChemFingerprintsc                   @   s@   e Zd Zddd�Zedd� �Zejdd� �Zd	d
� Zdd� ZdS )�FingerprintsCalculatorF�   �����c                 C   s   || _ || _|| _|| _d S �N)�n_cores�	fp_choise�to_numpy�FPSize)�selfr   r   r   r   � r   �Molecular_Representations.py�__init__7   s    zFingerprintsCalculator.__init__c                 C   s   | j S r   ��_ncores�r   r   r   r   r   =   s    zFingerprintsCalculator.n_coresc                 C   s�   d | _ |dkr|| _ nlzHt�� }|dkr8|| _ td� n$||krH|| _ ntd�|�� || _ W n" tk
r�   td� d| _ Y nX | j d k	s�t�d S �N�   r   z"multiprocessing is being executed.z8More cores than available requested! Falling back to {}!z>multiprocessing not supported. Falling back to single process!�r   �multiprocessing�	cpu_count�print�format�NotImplementedError�AssertionError�r   r   Zavailable_cpusr   r   r   r   A   s     

c                 C   s�   | j dkrtj|d| jd�}nN| j dkr:tj|| jd�}n2| j dkrlt�|�}d�dd	� |D ��}t	�
|�}| jr�t�d
t�}t	�||� |S |S d S )Nz	Morgan-FP�   )ZnBitszRDKit-FP)ZfpSizez
PubChem-FP� c                 S   s   g | ]}t |��qS r   )�str��.0�xr   r   r   �
<listcomp>`   s     z6FingerprintsCalculator.fp_as_array.<locals>.<listcomp>)r   )r   r   ZGetMorganFingerprintAsBitVectr   r   ZRDKFingerprintr   ZcalcPubChemFingerAll�joinr   ZCreateFromBitStringr   �npZzeros�intZConvertToNumpyArray)r   �mol�fpZ	bitstringZarrr   r   r   �fp_as_arrayX   s    




z"FingerprintsCalculator.fp_as_arrayc              	      sl   � j dkr� fdd�|D �S tj� j d��4}g }t|�� j|�t|�d�D ]}|�|� qJW 5 Q R X |S d S )Nr   c                    s   g | ]}� � |��qS r   )r1   �r)   r/   r   r   r   r+   n   s     z4FingerprintsCalculator.calculate.<locals>.<listcomp>�Z	processes��total)r   r   �Poolr   �imapr1   �len�append�r   ZmolsZpool�results�resultr   r   r   �	calculatek   s    
z FingerprintsCalculator.calculateN)Fr   r   )	�__name__�
__module__�__qualname__r   �propertyr   �setterr1   r=   r   r   r   r   r   6   s   


r   c                   @   sF   e Zd Zedfdd�Zedd� �Zejdd� �Zdd	d
�Zdd� Z	dS )�#ConstitutionalDescriptorsCalculatorr   c                 C   s   || _ || _d S r   )r   �constitutional_desc_list)r   rD   r   r   r   r   r   �   s    z,ConstitutionalDescriptorsCalculator.__init__c                 C   s   | j S r   r   r   r   r   r   r   �   s    z+ConstitutionalDescriptorsCalculator.n_coresc                 C   s�   d | _ |dkr|| _ nlzHt�� }|dkr8|| _ td� n$||krH|| _ ntd�|�� || _ W n" tk
r�   td� d| _ Y nX | j d k	s�t�d S r   r   r$   r   r   r   r   �   s     

NTc           
      C   sj   i }| j D ]B\}}z||�}W n$   |s:dd l}|��  |}Y nX |||< q
t�dd� |�� D ��}	|	S )Nr   c                 S   s   g | ]}|�qS r   r   r(   r   r   r   r+   �   s     z]ConstitutionalDescriptorsCalculator._calculate_constitutional_descriptors.<locals>.<listcomp>)rD   �	traceback�	print_excr-   �array�values)
r   r/   �
missingVal�silent�res�nm�fn�valrE   Zarray_cdr   r   r   �%_calculate_constitutional_descriptors�   s    

zIConstitutionalDescriptorsCalculator._calculate_constitutional_descriptorsc              	      sl   � j dkr� fdd�|D �S tj� j d��4}g }t|�� j|�t|�d�D ]}|�|� qJW 5 Q R X |S d S )Nr   c                    s   g | ]}� � |��qS r   )rO   r2   r   r   r   r+   �   s     zAConstitutionalDescriptorsCalculator.calculate.<locals>.<listcomp>r3   r4   )r   r   r6   r   r7   rO   r8   r9   r:   r   r   r   r=   �   s    
z-ConstitutionalDescriptorsCalculator.calculate)NT)
r>   r?   r@   rD   r   rA   r   rB   rO   r=   r   r   r   r   rC   �   s   


rC   c                   @   sF   e Zd Zedfdd�Zedd� �Zejdd� �Zdd	d
�Zdd� Z	dS )�RDKitDescriptorsCalculatorr   c                 C   s   || _ || _d S r   )r   �rdkit_desc_list)r   rQ   r   r   r   r   r   �   s    z#RDKitDescriptorsCalculator.__init__c                 C   s   | j S r   r   r   r   r   r   r   �   s    z"RDKitDescriptorsCalculator.n_coresc                 C   s�   d | _ |dkr|| _ nlzHt�� }|dkr8|| _ td� n$||krH|| _ ntd�|�� || _ W n" tk
r�   td� d| _ Y nX | j d k	s�t�d S r   r   r$   r   r   r   r   �   s     

NTc           
         sl   i }t jD ].\}}z||�}W n   |}Y nX |||< q
� fdd�|�� D �}t�dd� |�� D ��}	|	S )Nc                    s    i | ]\}}|� j kr||�qS r   )rQ   )r)   �keyrN   r   r   r   �
<dictcomp>�   s     
  zKRDKitDescriptorsCalculator._calculate_rdkit_descriptors.<locals>.<dictcomp>c                 S   s   g | ]}|�qS r   r   )r)   rN   r   r   r   r+   �   s     zKRDKitDescriptorsCalculator._calculate_rdkit_descriptors.<locals>.<listcomp>)r   Z	_descList�itemsr-   rG   rH   )
r   r/   rI   rJ   rK   rL   rM   rN   Zout_dictZ	out_arrayr   r   r   �_calculate_rdkit_descriptors�   s    

z7RDKitDescriptorsCalculator._calculate_rdkit_descriptorsc              	      sl   � j dkr� fdd�|D �S tj� j d��4}g }t|�� j|�t|�d�D ]}|�|� qJW 5 Q R X |S d S )Nr   c                    s   g | ]}� � |��qS r   )rU   r2   r   r   r   r+   �   s     z8RDKitDescriptorsCalculator.calculate.<locals>.<listcomp>r3   r4   )r   r   r6   r   r7   rU   r8   r9   r:   r   r   r   r=   �   s    
z$RDKitDescriptorsCalculator.calculate)NT)
r>   r?   r@   rQ   r   rA   r   rB   rU   r=   r   r   r   r   rP   �   s   


rP   c                   @   sD   e Zd Zedfdd�Zedd� �Zejdd� �Zdd� Zd	d
� Z	dS )�FunctionalGroupsCalculatorr   c                 C   s   || _ || _d S r   )r   �functional_groups)r   rW   r   r   r   r   r     s    z#FunctionalGroupsCalculator.__init__c                 C   s   | j S r   r   r   r   r   r   r     s    z"FunctionalGroupsCalculator.n_coresc                 C   s�   d | _ |dkr|| _ nlzHt�� }|dkr8|| _ td� n$||krH|| _ ntd�|�� || _ W n" tk
r�   td� d| _ Y nX | j d k	s�t�d S r   r   r$   r   r   r   r     s     

c                    s0   � fdd�| j D �}t�dd� |�� D ��}|S )Nc                    s   i | ]}|t t|�� ��qS r   )�getattrr   )r)   �name�r/   r   r   rS   0  s      zEFunctionalGroupsCalculator._get_functional_groups.<locals>.<dictcomp>c                 S   s   g | ]}|�qS r   r   r(   r   r   r   r+   1  s     zEFunctionalGroupsCalculator._get_functional_groups.<locals>.<listcomp>)rW   r-   rG   rH   )r   r/   r;   Zresults_arrayr   rZ   r   �_get_functional_groups.  s    z1FunctionalGroupsCalculator._get_functional_groupsc              	      sl   � j dkr� fdd�|D �S tj� j d��4}g }t|�� j|�t|�d�D ]}|�|� qJW 5 Q R X |S d S )Nr   c                    s   g | ]}� � |��qS r   )r[   r2   r   r   r   r+   8  s     z8FunctionalGroupsCalculator.calculate.<locals>.<listcomp>r3   r4   )r   r   r6   r   r7   r[   r8   r9   r:   r   r   r   r=   5  s    
z$FunctionalGroupsCalculator.calculateN)
r>   r?   r@   Zfunctional_groups_namesr   rA   r   rB   r[   r=   r   r   r   r   rV     s   

rV   )%Znumpyr-   r   Zrdkitr   Z
rdkit.Chemr   r   r   r   r   r   ZmathZjoblib�loadrQ   Zimportlib.machinery�	importlib�importlib.util�sysZpy_path�	machinery�SourcelessFileLoader�loader�util�spec_from_loaderrY   �spec�module_from_specr	   �exec_module�modulesr   r   rC   rP   rV   r   r   r   r   �<module>   s6   




P@H