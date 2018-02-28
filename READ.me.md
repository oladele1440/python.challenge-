

```python
import pandas as pd 
import numpy as np
```


```python
#importing file from the resource
data_file ="purchase_data.json"
```


```python
#reading the Json file from the resource 
data_file_df= pd.read_json(data_file)
data_file_df.head(10)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
    <tr>
      <th>5</th>
      <td>20</td>
      <td>Male</td>
      <td>10</td>
      <td>Sleepwalker</td>
      <td>1.73</td>
      <td>Tanimnya91</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20</td>
      <td>Male</td>
      <td>153</td>
      <td>Mercenary Sabre</td>
      <td>4.57</td>
      <td>Undjaskla97</td>
    </tr>
    <tr>
      <th>7</th>
      <td>29</td>
      <td>Female</td>
      <td>169</td>
      <td>Interrogator, Blood Blade of the Queen</td>
      <td>3.32</td>
      <td>Iathenudil29</td>
    </tr>
    <tr>
      <th>8</th>
      <td>25</td>
      <td>Male</td>
      <td>118</td>
      <td>Ghost Reaver, Longsword of Magic</td>
      <td>2.77</td>
      <td>Sondenasta63</td>
    </tr>
    <tr>
      <th>9</th>
      <td>31</td>
      <td>Male</td>
      <td>99</td>
      <td>Expiration, Warscythe Of Lost Worlds</td>
      <td>4.53</td>
      <td>Hilaerin92</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Find player count by finding unique screen names and finding the length of that list
player_count =len(data_file_df["SN"].unique())
player_count
```




    573




```python
#Creating Data Frame for Player Count
players_df = pd.DataFrame([{"Total Players": player_count}])
players_df.head(20)

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>




```python
#getting rid of number index and reseting the Total Players 
players_df.set_index('Total Players', inplace = True)
players_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
    </tr>
    <tr>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>573</th>
    </tr>
  </tbody>
</table>
</div>



# Purchasing Analysis (Total)


```python
#code for inspecting data
#pur_data['Item ID'].value_counts()
#unique_items = pd.DataFrame(pur_data['Item ID'].unique())
#len(unique_items)
```


```python
#creates a df but only keeping last occurance of Item ID
no_dup_items = data_file_df.drop_duplicates(['Item ID'], keep = 'last')
no_dup_items.head(10)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>17</th>
      <td>22</td>
      <td>Female</td>
      <td>59</td>
      <td>Lightning, Etcher of the King</td>
      <td>1.65</td>
      <td>Aenarap34</td>
    </tr>
    <tr>
      <th>21</th>
      <td>15</td>
      <td>Male</td>
      <td>3</td>
      <td>Phantomlight</td>
      <td>1.79</td>
      <td>Iaralrgue74</td>
    </tr>
    <tr>
      <th>59</th>
      <td>15</td>
      <td>Male</td>
      <td>2</td>
      <td>Verdict</td>
      <td>3.40</td>
      <td>Ila44</td>
    </tr>
    <tr>
      <th>63</th>
      <td>23</td>
      <td>Male</td>
      <td>28</td>
      <td>Flux, Destroyer of Due Diligence</td>
      <td>3.04</td>
      <td>Ryanara76</td>
    </tr>
    <tr>
      <th>88</th>
      <td>23</td>
      <td>Male</td>
      <td>132</td>
      <td>Persuasion</td>
      <td>3.90</td>
      <td>Undotesta33</td>
    </tr>
    <tr>
      <th>129</th>
      <td>23</td>
      <td>Female</td>
      <td>126</td>
      <td>Exiled Mithril Longsword</td>
      <td>3.25</td>
      <td>Eurinu48</td>
    </tr>
    <tr>
      <th>173</th>
      <td>30</td>
      <td>Male</td>
      <td>0</td>
      <td>Splinter</td>
      <td>1.82</td>
      <td>Chadadarya31</td>
    </tr>
    <tr>
      <th>177</th>
      <td>34</td>
      <td>Other / Non-Disclosed</td>
      <td>155</td>
      <td>War-Forged Gold Deflector</td>
      <td>3.73</td>
      <td>Assassa38</td>
    </tr>
    <tr>
      <th>185</th>
      <td>22</td>
      <td>Male</td>
      <td>167</td>
      <td>Malice, Legacy of the Queen</td>
      <td>2.38</td>
      <td>Siarinum43</td>
    </tr>
    <tr>
      <th>196</th>
      <td>20</td>
      <td>Male</td>
      <td>89</td>
      <td>Blazefury, Protector of Delusions</td>
      <td>1.50</td>
      <td>Chanirra56</td>
    </tr>
  </tbody>
</table>
</div>




```python
#counts items by unique ID
total_unique = len(no_dup_items)
total_unique
```




    183




```python
#calculating the totlal average
total_purchase = data_file_df['Price'].count()
total_revenue = round(data_file_df['Price'].sum(),2)
average_price = round(total_revenue/total_purchase, 2)
average_price
```




    2.9300000000000002




```python
#finds the number of total purchases by counting occurances of price
total_purchase = data_file_df['Price'].count()
total_purchase
```




    780




```python
#calculates total revenue for table by summing occurance of price and below calc
total_revenue = round(data_file_df['Price'].sum(),2)
total_revenue
```




    2286.33




```python
#creates Purchase Analysis DataFrame
```


```python
pur_analysis = pd.DataFrame([{"Number of Unique Items": total_unique,
                              "Average Purchase Price": average_price,
                              "Total Purchases": total_purchase,
                              "Total Revenue": total_revenue}])
pur_analysis
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Number of Unique Items</th>
      <th>Total Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.93</td>
      <td>183</td>
      <td>780</td>
      <td>2286.33</td>
    </tr>
  </tbody>
</table>
</div>



# Gender Demographics



```python
# Percentage and Count of Male Players
# Percentage and Count of Female Players
# Percentage and Count of Other / Non-Disclosed
```


```python
#creates df of unique player names by only keeping the last occurance
no_dup_players = data_file_df.drop_duplicates(['SN'], keep ='last')
no_dup_players.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
    <tr>
      <th>5</th>
      <td>20</td>
      <td>Male</td>
      <td>10</td>
      <td>Sleepwalker</td>
      <td>1.73</td>
      <td>Tanimnya91</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20</td>
      <td>Male</td>
      <td>153</td>
      <td>Mercenary Sabre</td>
      <td>4.57</td>
      <td>Undjaskla97</td>
    </tr>
  </tbody>
</table>
</div>




```python
#counts gender values from the df with no duplicate screen names
gender_counts = no_dup_players["Gender"].value_counts().reset_index()
gender_counts.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>Gender</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Male</td>
      <td>465</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Female</td>
      <td>100</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Other / Non-Disclosed</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
#adds column for % of players using player count from first table and gender_count 
#column which is a count from line above
gender_count_percentage = gender_counts['Gender']/player_count * 100
gender_count_percentage
```




    0    81.151832
    1    17.452007
    2     1.396161
    Name: Gender, dtype: float64




```python
#renaming of the column
gender_counts.rename(columns = {'index': 'Gender', 'Gender': '# of Players'}, inplace = True)
gender_counts
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
      <th># of Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Male</td>
      <td>465</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Female</td>
      <td>100</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Other / Non-Disclosed</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
#sets index as Gender for aesthetics 
gender_counts.set_index(['Gender'], inplace = True)
gender_counts
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th># of Players</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>465</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>100</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
#just checking percents sum to 100%
#gender_counts['% of Players'].sum()
#formats table
gender_counts.style.format({"% of Players": "{:.1f}%"})
```




<style  type="text/css" >
</style>  
<table id="T_0ec66ae8_1bea_11e8_8a3b_b0359fca2b09" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" ># of Players</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Gender</th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_0ec66ae8_1bea_11e8_8a3b_b0359fca2b09level0_row0" class="row_heading level0 row0" >Male</th> 
        <td id="T_0ec66ae8_1bea_11e8_8a3b_b0359fca2b09row0_col0" class="data row0 col0" >465</td> 
    </tr>    <tr> 
        <th id="T_0ec66ae8_1bea_11e8_8a3b_b0359fca2b09level0_row1" class="row_heading level0 row1" >Female</th> 
        <td id="T_0ec66ae8_1bea_11e8_8a3b_b0359fca2b09row1_col0" class="data row1 col0" >100</td> 
    </tr>    <tr> 
        <th id="T_0ec66ae8_1bea_11e8_8a3b_b0359fca2b09level0_row2" class="row_heading level0 row2" >Other / Non-Disclosed</th> 
        <td id="T_0ec66ae8_1bea_11e8_8a3b_b0359fca2b09row2_col0" class="data row2 col0" >8</td> 
    </tr></tbody> 
</table> 



# Purchasing Analysis by Gender


```python
# Purchasing Analysis (Gender)
# The below each broken by gender
# Purchase Count
# Average Purchase Price
# Total Purchase Value
# Normalized Totals
```


```python
# counts purchases by gender
pur_count_gender = pd.DataFrame(data_file_df.groupby('Gender')['Gender'].count())
pur_count_gender
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Sum of Total purchase of Value
total_pur_value = pd.DataFrame(data_file_df.groupby('Gender')['Price'].sum())
total_pur_value
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>382.91</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>1867.68</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>35.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
#merging the two data frames from above that is the Purchase Count and Total Purchase Value
purchase_analysis = pd.merge(pur_count_gender, total_pur_value, left_index = True, right_index = True)
purchase_analysis
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
      <th>Price</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>382.91</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>1867.68</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>35.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
#renaming the columns
purchase_analysis.rename(columns = {'Gender': 'Purchases', 'Price':'Total Purchase Value'}, inplace=True)
purchase_analysis
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchases</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>382.91</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>1867.68</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>35.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
#adds column for average purchase price by gender by dividing total purcahse value by gender by # of purchases by gender
purchase_analysis['Average Purchase Price'] = purchase_analysis['Total Purchase Value']/purchase_analysis['Purchases']
purchase_analysis
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchases</th>
      <th>Total Purchase Value</th>
      <th>Average Purchase Price</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>382.91</td>
      <td>2.815515</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>1867.68</td>
      <td>2.950521</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>35.74</td>
      <td>3.249091</td>
    </tr>
  </tbody>
</table>
</div>




```python
purchase_analysis['Normalized Totals'] = purchase_analysis['Total Purchase Value']/purchase_analysis['Purchases'] 
purchase_analysis
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchases</th>
      <th>Total Purchase Value</th>
      <th>Average Purchase Price</th>
      <th>Gender</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>382.91</td>
      <td>2.815515</td>
      <td>136</td>
      <td>2.815515</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>1867.68</td>
      <td>2.950521</td>
      <td>633</td>
      <td>2.950521</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>35.74</td>
      <td>3.249091</td>
      <td>11</td>
      <td>3.249091</td>
    </tr>
  </tbody>
</table>
</div>




```python
purchase_analysis.style.format({'Total Purchase Value': '${:.2f}', 
                               'Average Purchase Price': '${:.2f}', 'Normalized Totals': '${:.2f}'})
```




<style  type="text/css" >
</style>  
<table id="T_92a6b088_1c03_11e8_9853_b0359fca2b09" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Purchases</th> 
        <th class="col_heading level0 col1" >Total Purchase Value</th> 
        <th class="col_heading level0 col2" >Average Purchase Price</th> 
        <th class="col_heading level0 col3" >Normalized Totals</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Gender</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_92a6b088_1c03_11e8_9853_b0359fca2b09level0_row0" class="row_heading level0 row0" >Female</th> 
        <td id="T_92a6b088_1c03_11e8_9853_b0359fca2b09row0_col0" class="data row0 col0" >136</td> 
        <td id="T_92a6b088_1c03_11e8_9853_b0359fca2b09row0_col1" class="data row0 col1" >$382.91</td> 
        <td id="T_92a6b088_1c03_11e8_9853_b0359fca2b09row0_col2" class="data row0 col2" >$2.82</td> 
        <td id="T_92a6b088_1c03_11e8_9853_b0359fca2b09row0_col3" class="data row0 col3" >$2.82</td> 
    </tr>    <tr> 
        <th id="T_92a6b088_1c03_11e8_9853_b0359fca2b09level0_row1" class="row_heading level0 row1" >Male</th> 
        <td id="T_92a6b088_1c03_11e8_9853_b0359fca2b09row1_col0" class="data row1 col0" >633</td> 
        <td id="T_92a6b088_1c03_11e8_9853_b0359fca2b09row1_col1" class="data row1 col1" >$1867.68</td> 
        <td id="T_92a6b088_1c03_11e8_9853_b0359fca2b09row1_col2" class="data row1 col2" >$2.95</td> 
        <td id="T_92a6b088_1c03_11e8_9853_b0359fca2b09row1_col3" class="data row1 col3" >$2.95</td> 
    </tr>    <tr> 
        <th id="T_92a6b088_1c03_11e8_9853_b0359fca2b09level0_row2" class="row_heading level0 row2" >Other / Non-Disclosed</th> 
        <td id="T_92a6b088_1c03_11e8_9853_b0359fca2b09row2_col0" class="data row2 col0" >11</td> 
        <td id="T_92a6b088_1c03_11e8_9853_b0359fca2b09row2_col1" class="data row2 col1" >$35.74</td> 
        <td id="T_92a6b088_1c03_11e8_9853_b0359fca2b09row2_col2" class="data row2 col2" >$3.25</td> 
        <td id="T_92a6b088_1c03_11e8_9853_b0359fca2b09row2_col3" class="data row2 col3" >$3.25</td> 
    </tr></tbody> 
</table> 




```python
del purchase_analysis["Gender"]
purchase_analysis
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchases</th>
      <th>Total Purchase Value</th>
      <th>Average Purchase Price</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>382.91</td>
      <td>2.815515</td>
      <td>2.815515</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>1867.68</td>
      <td>2.950521</td>
      <td>2.950521</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>35.74</td>
      <td>3.249091</td>
      <td>3.249091</td>
    </tr>
  </tbody>
</table>
</div>



# Age Demographics


```python
# The below each broken into bins of 4 years (i.e. <10, 10-14, 15-19, etc.)
# Purchase Count
# Average Purchase Price
# Total Purchase Value
# Normalized Totals
```


```python
#creates a column 'age_bin' based on conditional of age range
data_file_df.loc[(data_file_df['Age'] < 10), 'age_bin'] = "< 10"
data_file_df.loc[(data_file_df['Age'] >= 10) & (data_file_df['Age'] <= 14), 'age_bin'] = "10 - 14"
data_file_df.loc[(data_file_df['Age'] >= 15) & (data_file_df['Age'] <= 19), 'age_bin'] = "15 - 19"
data_file_df.loc[(data_file_df['Age'] >= 20) & (data_file_df['Age'] <= 24), 'age_bin'] = "20 - 24"
data_file_df.loc[(data_file_df['Age'] >= 25) & (data_file_df['Age'] <= 29), 'age_bin'] = "25 - 29"
data_file_df.loc[(data_file_df['Age'] >= 30) & (data_file_df['Age'] <= 34), 'age_bin'] = "30 - 34"
data_file_df.loc[(data_file_df['Age'] >= 35) & (data_file_df['Age'] <= 39), 'age_bin'] = "35 - 39"
data_file_df.loc[(data_file_df['Age'] >= 40), 'age_bin'] = "> 40"

data_file_df[['age_bin', 'Age']].count()
```




    age_bin    780
    Age        780
    dtype: int64




```python
# counts purchases by age bin by counting screen names (non-unique)
pur_count_age = pd.DataFrame(data_file_df.groupby('age_bin')['SN'].count())
pur_count_age
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SN</th>
    </tr>
    <tr>
      <th>age_bin</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10 - 14</th>
      <td>35</td>
    </tr>
    <tr>
      <th>15 - 19</th>
      <td>133</td>
    </tr>
    <tr>
      <th>20 - 24</th>
      <td>336</td>
    </tr>
    <tr>
      <th>25 - 29</th>
      <td>125</td>
    </tr>
    <tr>
      <th>30 - 34</th>
      <td>64</td>
    </tr>
    <tr>
      <th>35 - 39</th>
      <td>42</td>
    </tr>
    <tr>
      <th>&lt; 10</th>
      <td>28</td>
    </tr>
    <tr>
      <th>&gt; 40</th>
      <td>17</td>
    </tr>
  </tbody>
</table>
</div>




```python
#finds avg price of purchases by age bin
avg_price_age = pd.DataFrame(data_file_df.groupby('age_bin')['Price'].mean())
avg_price_age
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
    </tr>
    <tr>
      <th>age_bin</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10 - 14</th>
      <td>2.770000</td>
    </tr>
    <tr>
      <th>15 - 19</th>
      <td>2.905414</td>
    </tr>
    <tr>
      <th>20 - 24</th>
      <td>2.913006</td>
    </tr>
    <tr>
      <th>25 - 29</th>
      <td>2.962640</td>
    </tr>
    <tr>
      <th>30 - 34</th>
      <td>3.082031</td>
    </tr>
    <tr>
      <th>35 - 39</th>
      <td>2.842857</td>
    </tr>
    <tr>
      <th>&lt; 10</th>
      <td>2.980714</td>
    </tr>
    <tr>
      <th>&gt; 40</th>
      <td>3.161765</td>
    </tr>
  </tbody>
</table>
</div>




```python
#finds total purchase value by age bintgv
tot_pur_age = pd.DataFrame(data_file_df.groupby('age_bin')['Price'].sum())
tot_pur_age
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
    </tr>
    <tr>
      <th>age_bin</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10 - 14</th>
      <td>96.95</td>
    </tr>
    <tr>
      <th>15 - 19</th>
      <td>386.42</td>
    </tr>
    <tr>
      <th>20 - 24</th>
      <td>978.77</td>
    </tr>
    <tr>
      <th>25 - 29</th>
      <td>370.33</td>
    </tr>
    <tr>
      <th>30 - 34</th>
      <td>197.25</td>
    </tr>
    <tr>
      <th>35 - 39</th>
      <td>119.40</td>
    </tr>
    <tr>
      <th>&lt; 10</th>
      <td>83.46</td>
    </tr>
    <tr>
      <th>&gt; 40</th>
      <td>53.75</td>
    </tr>
  </tbody>
</table>
</div>




```python
#deletes multiple occurances of SN while only keeping last, then counts # of unique
#players by age bin
no_dup_age = pd.DataFrame(data_file_df.drop_duplicates('SN', keep = 'last').groupby('age_bin')['SN'].count())
no_dup_age
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SN</th>
    </tr>
    <tr>
      <th>age_bin</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10 - 14</th>
      <td>23</td>
    </tr>
    <tr>
      <th>15 - 19</th>
      <td>100</td>
    </tr>
    <tr>
      <th>20 - 24</th>
      <td>259</td>
    </tr>
    <tr>
      <th>25 - 29</th>
      <td>87</td>
    </tr>
    <tr>
      <th>30 - 34</th>
      <td>47</td>
    </tr>
    <tr>
      <th>35 - 39</th>
      <td>27</td>
    </tr>
    <tr>
      <th>&lt; 10</th>
      <td>19</td>
    </tr>
    <tr>
      <th>&gt; 40</th>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
#merging all above DataFrames
merge_age = pd.merge(pur_count_age, avg_price_age, left_index = True, right_index = True).merge(tot_pur_age, left_index = True, right_index = True).merge(no_dup_age, left_index = True, right_index = True)
merge_age
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SN_x</th>
      <th>Price_x</th>
      <th>Price_y</th>
      <th>SN_y</th>
    </tr>
    <tr>
      <th>age_bin</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10 - 14</th>
      <td>35</td>
      <td>2.770000</td>
      <td>96.95</td>
      <td>23</td>
    </tr>
    <tr>
      <th>15 - 19</th>
      <td>133</td>
      <td>2.905414</td>
      <td>386.42</td>
      <td>100</td>
    </tr>
    <tr>
      <th>20 - 24</th>
      <td>336</td>
      <td>2.913006</td>
      <td>978.77</td>
      <td>259</td>
    </tr>
    <tr>
      <th>25 - 29</th>
      <td>125</td>
      <td>2.962640</td>
      <td>370.33</td>
      <td>87</td>
    </tr>
    <tr>
      <th>30 - 34</th>
      <td>64</td>
      <td>3.082031</td>
      <td>197.25</td>
      <td>47</td>
    </tr>
    <tr>
      <th>35 - 39</th>
      <td>42</td>
      <td>2.842857</td>
      <td>119.40</td>
      <td>27</td>
    </tr>
    <tr>
      <th>&lt; 10</th>
      <td>28</td>
      <td>2.980714</td>
      <td>83.46</td>
      <td>19</td>
    </tr>
    <tr>
      <th>&gt; 40</th>
      <td>17</td>
      <td>3.161765</td>
      <td>53.75</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
#renaming the columns
merge_age.rename(columns = {"SN_x": "number of Purchases", "Price_x": "Average Purchase Price", "Price_y": "Total Purchase Value", "SN_y": "number of Purchasers"}, inplace = True)
merge_age
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>number of Purchases</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>number of Purchasers</th>
    </tr>
    <tr>
      <th>age_bin</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10 - 14</th>
      <td>35</td>
      <td>2.770000</td>
      <td>96.95</td>
      <td>23</td>
    </tr>
    <tr>
      <th>15 - 19</th>
      <td>133</td>
      <td>2.905414</td>
      <td>386.42</td>
      <td>100</td>
    </tr>
    <tr>
      <th>20 - 24</th>
      <td>336</td>
      <td>2.913006</td>
      <td>978.77</td>
      <td>259</td>
    </tr>
    <tr>
      <th>25 - 29</th>
      <td>125</td>
      <td>2.962640</td>
      <td>370.33</td>
      <td>87</td>
    </tr>
    <tr>
      <th>30 - 34</th>
      <td>64</td>
      <td>3.082031</td>
      <td>197.25</td>
      <td>47</td>
    </tr>
    <tr>
      <th>35 - 39</th>
      <td>42</td>
      <td>2.842857</td>
      <td>119.40</td>
      <td>27</td>
    </tr>
    <tr>
      <th>&lt; 10</th>
      <td>28</td>
      <td>2.980714</td>
      <td>83.46</td>
      <td>19</td>
    </tr>
    <tr>
      <th>&gt; 40</th>
      <td>17</td>
      <td>3.161765</td>
      <td>53.75</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
#calculating normalized totals
normalized_totals = merge_age['Normalized Totals'] = merge_age['Total Purchase Value']/merge_age['number of Purchasers']
normalized_totals
```




    Age
    10 - 14    4.215217
    15 - 19    3.864200
    20 - 24    3.779035
    25 - 29    4.256667
    30 - 34    4.196809
    35 - 39    4.422222
    < 10       4.392632
    > 40       4.886364
    dtype: float64




```python
#resetting index for aesthetics
index_merge = merge_age.index.rename("Age", inplace = True)
index_merge
```


```python
# formats
format_merge = merge_age.style.format({'Average Purchase Price': '${:.2f}', 'Total Purchase Value': '${:.2f}', 'Normalized Totals': '${:.2f}'})
format_merge
```




<style  type="text/css" >
</style>  
<table id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >number of Purchases</th> 
        <th class="col_heading level0 col1" >Average Purchase Price</th> 
        <th class="col_heading level0 col2" >Total Purchase Value</th> 
        <th class="col_heading level0 col3" >number of Purchasers</th> 
        <th class="col_heading level0 col4" >Normalized Totals</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Age</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09level0_row0" class="row_heading level0 row0" >10 - 14</th> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row0_col0" class="data row0 col0" >35</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row0_col1" class="data row0 col1" >$2.77</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row0_col2" class="data row0 col2" >$96.95</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row0_col3" class="data row0 col3" >23</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row0_col4" class="data row0 col4" >$4.22</td> 
    </tr>    <tr> 
        <th id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09level0_row1" class="row_heading level0 row1" >15 - 19</th> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row1_col0" class="data row1 col0" >133</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row1_col1" class="data row1 col1" >$2.91</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row1_col2" class="data row1 col2" >$386.42</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row1_col3" class="data row1 col3" >100</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row1_col4" class="data row1 col4" >$3.86</td> 
    </tr>    <tr> 
        <th id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09level0_row2" class="row_heading level0 row2" >20 - 24</th> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row2_col0" class="data row2 col0" >336</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row2_col1" class="data row2 col1" >$2.91</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row2_col2" class="data row2 col2" >$978.77</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row2_col3" class="data row2 col3" >259</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row2_col4" class="data row2 col4" >$3.78</td> 
    </tr>    <tr> 
        <th id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09level0_row3" class="row_heading level0 row3" >25 - 29</th> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row3_col0" class="data row3 col0" >125</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row3_col1" class="data row3 col1" >$2.96</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row3_col2" class="data row3 col2" >$370.33</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row3_col3" class="data row3 col3" >87</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row3_col4" class="data row3 col4" >$4.26</td> 
    </tr>    <tr> 
        <th id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09level0_row4" class="row_heading level0 row4" >30 - 34</th> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row4_col0" class="data row4 col0" >64</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row4_col1" class="data row4 col1" >$3.08</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row4_col2" class="data row4 col2" >$197.25</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row4_col3" class="data row4 col3" >47</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row4_col4" class="data row4 col4" >$4.20</td> 
    </tr>    <tr> 
        <th id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09level0_row5" class="row_heading level0 row5" >35 - 39</th> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row5_col0" class="data row5 col0" >42</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row5_col1" class="data row5 col1" >$2.84</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row5_col2" class="data row5 col2" >$119.40</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row5_col3" class="data row5 col3" >27</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row5_col4" class="data row5 col4" >$4.42</td> 
    </tr>    <tr> 
        <th id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09level0_row6" class="row_heading level0 row6" >< 10</th> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row6_col0" class="data row6 col0" >28</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row6_col1" class="data row6 col1" >$2.98</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row6_col2" class="data row6 col2" >$83.46</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row6_col3" class="data row6 col3" >19</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row6_col4" class="data row6 col4" >$4.39</td> 
    </tr>    <tr> 
        <th id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09level0_row7" class="row_heading level0 row7" >> 40</th> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row7_col0" class="data row7 col0" >17</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row7_col1" class="data row7 col1" >$3.16</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row7_col2" class="data row7 col2" >$53.75</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row7_col3" class="data row7 col3" >11</td> 
        <td id="T_1297c5ac_1c0b_11e8_a801_b0359fca2b09row7_col4" class="data row7 col4" >$4.89</td> 
    </tr></tbody> 
</table> 



# Top Spenders


```python
# Identify the the top 5 spenders in the game by total purchase value, then list (in a table):
# SN
# Purchase Count
# Average Purchase Price
# Total Purchase Value
```


```python
#Group by screen name to find, total purchase per person, number of purchases per person, and average price price per person
purchase_amt_by_SN = pd.DataFrame(data_file_df.groupby('SN')['Price'].sum())
num_purchase_by_SN = pd.DataFrame(data_file_df.groupby('SN')['Price'].count())
avg_purchase_by_SN = pd.DataFrame(data_file_df.groupby('SN')['Price'].mean())
```


```python
# merge the above dfs
merged_top5 = pd.merge(purchase_amt_by_SN, num_purchase_by_SN, left_index = True, right_index = True).merge(avg_purchase_by_SN, left_index=True, right_index=True)
merged_top5.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price_x</th>
      <th>Price_y</th>
      <th>Price</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Adairialis76</th>
      <td>2.46</td>
      <td>1</td>
      <td>2.460000</td>
    </tr>
    <tr>
      <th>Aduephos78</th>
      <td>6.70</td>
      <td>3</td>
      <td>2.233333</td>
    </tr>
    <tr>
      <th>Aeduera68</th>
      <td>5.80</td>
      <td>3</td>
      <td>1.933333</td>
    </tr>
    <tr>
      <th>Aela49</th>
      <td>2.46</td>
      <td>1</td>
      <td>2.460000</td>
    </tr>
    <tr>
      <th>Aela59</th>
      <td>1.27</td>
      <td>1</td>
      <td>1.270000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# renaming the columns
merged_top5.rename(columns = {'Price_x': 'Total Purchase Value', 'Price_y':'Purchase Count', 'Price':'Average Purchase Price'}, inplace = True)
merged_top5.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Purchase Value</th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Adairialis76</th>
      <td>2.46</td>
      <td>1</td>
      <td>2.460000</td>
    </tr>
    <tr>
      <th>Aduephos78</th>
      <td>6.70</td>
      <td>3</td>
      <td>2.233333</td>
    </tr>
    <tr>
      <th>Aeduera68</th>
      <td>5.80</td>
      <td>3</td>
      <td>1.933333</td>
    </tr>
    <tr>
      <th>Aela49</th>
      <td>2.46</td>
      <td>1</td>
      <td>2.460000</td>
    </tr>
    <tr>
      <th>Aela59</th>
      <td>1.27</td>
      <td>1</td>
      <td>1.270000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# sort from highest purchase value to lowest
merged_top5.sort_values('Total Purchase Value', ascending = False, inplace=True)
merged_top5.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Purchase Value</th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>17.06</td>
      <td>5</td>
      <td>3.412000</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>13.56</td>
      <td>4</td>
      <td>3.390000</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>12.74</td>
      <td>4</td>
      <td>3.185000</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>12.73</td>
      <td>3</td>
      <td>4.243333</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>11.58</td>
      <td>3</td>
      <td>3.860000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# format
merged_top5.style.format({'Total Purchase Value': '${:.2f}', 'Average Purchase Price': '${:.2f}'})
```




<style  type="text/css" >
</style>  
<table id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Total Purchase Value</th> 
        <th class="col_heading level0 col1" >Purchase Count</th> 
        <th class="col_heading level0 col2" >Average Purchase Price</th> 
    </tr>    <tr> 
        <th class="index_name level0" >SN</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row0" class="row_heading level0 row0" >Undirrala66</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row0_col0" class="data row0 col0" >$17.06</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row0_col1" class="data row0 col1" >5</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row0_col2" class="data row0 col2" >$3.41</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row1" class="row_heading level0 row1" >Saedue76</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row1_col0" class="data row1 col0" >$13.56</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row1_col1" class="data row1 col1" >4</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row1_col2" class="data row1 col2" >$3.39</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row2" class="row_heading level0 row2" >Mindimnya67</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row2_col0" class="data row2 col0" >$12.74</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row2_col1" class="data row2 col1" >4</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row2_col2" class="data row2 col2" >$3.18</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row3" class="row_heading level0 row3" >Haellysu29</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row3_col0" class="data row3 col0" >$12.73</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row3_col1" class="data row3 col1" >3</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row3_col2" class="data row3 col2" >$4.24</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row4" class="row_heading level0 row4" >Eoda93</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row4_col0" class="data row4 col0" >$11.58</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row4_col1" class="data row4 col1" >3</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row4_col2" class="data row4 col2" >$3.86</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row5" class="row_heading level0 row5" >Isursti83</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row5_col0" class="data row5 col0" >$11.05</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row5_col1" class="data row5 col1" >3</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row5_col2" class="data row5 col2" >$3.68</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row6" class="row_heading level0 row6" >Isurria36</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row6_col0" class="data row6 col0" >$11.01</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row6_col1" class="data row6 col1" >3</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row6_col2" class="data row6 col2" >$3.67</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row7" class="row_heading level0 row7" >Eusri70</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row7_col0" class="data row7 col0" >$10.55</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row7_col1" class="data row7 col1" >3</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row7_col2" class="data row7 col2" >$3.52</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row8" class="row_heading level0 row8" >Aerithllora36</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row8_col0" class="data row8 col0" >$10.45</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row8_col1" class="data row8 col1" >3</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row8_col2" class="data row8 col2" >$3.48</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row9" class="row_heading level0 row9" >Yasriphos60</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row9_col0" class="data row9 col0" >$10.40</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row9_col1" class="data row9 col1" >3</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row9_col2" class="data row9 col2" >$3.47</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row10" class="row_heading level0 row10" >Sondastan54</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row10_col0" class="data row10 col0" >$10.24</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row10_col1" class="data row10 col1" >4</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row10_col2" class="data row10 col2" >$2.56</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row11" class="row_heading level0 row11" >Haerith37</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row11_col0" class="data row11 col0" >$10.14</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row11_col1" class="data row11 col1" >3</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row11_col2" class="data row11 col2" >$3.38</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row12" class="row_heading level0 row12" >Chadjask77</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row12_col0" class="data row12 col0" >$10.01</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row12_col1" class="data row12 col1" >3</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row12_col2" class="data row12 col2" >$3.34</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row13" class="row_heading level0 row13" >Qarwen67</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row13_col0" class="data row13 col0" >$9.97</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row13_col1" class="data row13 col1" >4</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row13_col2" class="data row13 col2" >$2.49</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row14" class="row_heading level0 row14" >Sondim43</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row14_col0" class="data row14 col0" >$9.38</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row14_col1" class="data row14 col1" >3</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row14_col2" class="data row14 col2" >$3.13</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row15" class="row_heading level0 row15" >Tillyrin30</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row15_col0" class="data row15 col0" >$9.19</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row15_col1" class="data row15 col1" >3</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row15_col2" class="data row15 col2" >$3.06</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row16" class="row_heading level0 row16" >Lisistaya47</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row16_col0" class="data row16 col0" >$9.19</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row16_col1" class="data row16 col1" >3</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row16_col2" class="data row16 col2" >$3.06</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row17" class="row_heading level0 row17" >Tyisriphos58</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row17_col0" class="data row17 col0" >$9.18</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row17_col1" class="data row17 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row17_col2" class="data row17 col2" >$4.59</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row18" class="row_heading level0 row18" >Frichaya88</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row18_col0" class="data row18 col0" >$9.16</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row18_col1" class="data row18 col1" >3</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row18_col2" class="data row18 col2" >$3.05</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row19" class="row_heading level0 row19" >Assassasta79</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row19_col0" class="data row19 col0" >$9.12</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row19_col1" class="data row19 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row19_col2" class="data row19 col2" >$4.56</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row20" class="row_heading level0 row20" >Lisossan98</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row20_col0" class="data row20 col0" >$9.10</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row20_col1" class="data row20 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row20_col2" class="data row20 col2" >$4.55</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row21" class="row_heading level0 row21" >Yadanun74</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row21_col0" class="data row21 col0" >$9.09</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row21_col1" class="data row21 col1" >3</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row21_col2" class="data row21 col2" >$3.03</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row22" class="row_heading level0 row22" >Mindirra92</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row22_col0" class="data row22 col0" >$9.01</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row22_col1" class="data row22 col1" >3</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row22_col2" class="data row22 col2" >$3.00</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row23" class="row_heading level0 row23" >Aeliru63</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row23_col0" class="data row23 col0" >$8.98</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row23_col1" class="data row23 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row23_col2" class="data row23 col2" >$4.49</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row24" class="row_heading level0 row24" >Chanastsda67</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row24_col0" class="data row24 col0" >$8.96</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row24_col1" class="data row24 col1" >3</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row24_col2" class="data row24 col2" >$2.99</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row25" class="row_heading level0 row25" >Frichosiala98</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row25_col0" class="data row25 col0" >$8.94</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row25_col1" class="data row25 col1" >3</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row25_col2" class="data row25 col2" >$2.98</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row26" class="row_heading level0 row26" >Malunil62</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row26_col0" class="data row26 col0" >$8.89</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row26_col1" class="data row26 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row26_col2" class="data row26 col2" >$4.45</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row27" class="row_heading level0 row27" >Iskadarya95</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row27_col0" class="data row27 col0" >$8.79</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row27_col1" class="data row27 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row27_col2" class="data row27 col2" >$4.39</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row28" class="row_heading level0 row28" >Ilogha82</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row28_col0" class="data row28 col0" >$8.61</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row28_col1" class="data row28 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row28_col2" class="data row28 col2" >$4.30</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row29" class="row_heading level0 row29" >Yadaisuir65</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row29_col0" class="data row29 col0" >$8.56</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row29_col1" class="data row29 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row29_col2" class="data row29 col2" >$4.28</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row30" class="row_heading level0 row30" >Indcil77</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row30_col0" class="data row30 col0" >$8.53</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row30_col1" class="data row30 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row30_col2" class="data row30 col2" >$4.27</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row31" class="row_heading level0 row31" >Haedasu65</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row31_col0" class="data row31 col0" >$8.49</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row31_col1" class="data row31 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row31_col2" class="data row31 col2" >$4.25</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row32" class="row_heading level0 row32" >Ingatcil75</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row32_col0" class="data row32 col0" >$8.44</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row32_col1" class="data row32 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row32_col2" class="data row32 col2" >$4.22</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row33" class="row_heading level0 row33" >Narirra38</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row33_col0" class="data row33 col0" >$8.42</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row33_col1" class="data row33 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row33_col2" class="data row33 col2" >$4.21</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row34" class="row_heading level0 row34" >Seorithstilis90</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row34_col0" class="data row34 col0" >$8.39</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row34_col1" class="data row34 col1" >3</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row34_col2" class="data row34 col2" >$2.80</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row35" class="row_heading level0 row35" >Lirtosia72</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row35_col0" class="data row35 col0" >$8.37</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row35_col1" class="data row35 col1" >3</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row35_col2" class="data row35 col2" >$2.79</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row36" class="row_heading level0 row36" >Eurisuru25</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row36_col0" class="data row36 col0" >$8.29</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row36_col1" class="data row36 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row36_col2" class="data row36 col2" >$4.14</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row37" class="row_heading level0 row37" >Shaidanu32</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row37_col0" class="data row37 col0" >$8.25</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row37_col1" class="data row37 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row37_col2" class="data row37 col2" >$4.12</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row38" class="row_heading level0 row38" >Jiskossa51</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row38_col0" class="data row38 col0" >$8.14</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row38_col1" class="data row38 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row38_col2" class="data row38 col2" >$4.07</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row39" class="row_heading level0 row39" >Lassjaskan73</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row39_col0" class="data row39 col0" >$7.98</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row39_col1" class="data row39 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row39_col2" class="data row39 col2" >$3.99</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row40" class="row_heading level0 row40" >Ethrusuard41</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row40_col0" class="data row40 col0" >$7.93</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row40_col1" class="data row40 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row40_col2" class="data row40 col2" >$3.96</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row41" class="row_heading level0 row41" >Chadossa56</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row41_col0" class="data row41 col0" >$7.85</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row41_col1" class="data row41 col1" >3</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row41_col2" class="data row41 col2" >$2.62</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row42" class="row_heading level0 row42" >Ila44</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row42_col0" class="data row42 col0" >$7.84</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row42_col1" class="data row42 col1" >3</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row42_col2" class="data row42 col2" >$2.61</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row43" class="row_heading level0 row43" >Yathecal72</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row43_col0" class="data row43 col0" >$7.77</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row43_col1" class="data row43 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row43_col2" class="data row43 col2" >$3.88</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row44" class="row_heading level0 row44" >Eural50</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row44_col0" class="data row44 col0" >$7.68</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row44_col1" class="data row44 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row44_col2" class="data row44 col2" >$3.84</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row45" class="row_heading level0 row45" >Lisjaskan36</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row45_col0" class="data row45 col0" >$7.68</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row45_col1" class="data row45 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row45_col2" class="data row45 col2" >$3.84</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row46" class="row_heading level0 row46" >Reula64</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row46_col0" class="data row46 col0" >$7.57</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row46_col1" class="data row46 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row46_col2" class="data row46 col2" >$3.79</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row47" class="row_heading level0 row47" >Airi27</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row47_col0" class="data row47 col0" >$7.57</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row47_col1" class="data row47 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row47_col2" class="data row47 col2" >$3.79</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row48" class="row_heading level0 row48" >Sondossa55</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row48_col0" class="data row48 col0" >$7.44</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row48_col1" class="data row48 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row48_col2" class="data row48 col2" >$3.72</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row49" class="row_heading level0 row49" >Ililsa62</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row49_col0" class="data row49 col0" >$7.40</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row49_col1" class="data row49 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row49_col2" class="data row49 col2" >$3.70</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row50" class="row_heading level0 row50" >Tyadaru49</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row50_col0" class="data row50 col0" >$7.36</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row50_col1" class="data row50 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row50_col2" class="data row50 col2" >$3.68</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row51" class="row_heading level0 row51" >Ialistidru50</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row51_col0" class="data row51 col0" >$7.34</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row51_col1" class="data row51 col1" >3</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row51_col2" class="data row51 col2" >$2.45</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row52" class="row_heading level0 row52" >Deural48</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row52_col0" class="data row52 col0" >$7.27</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row52_col1" class="data row52 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row52_col2" class="data row52 col2" >$3.63</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row53" class="row_heading level0 row53" >Eosurdru76</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row53_col0" class="data row53 col0" >$7.24</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row53_col1" class="data row53 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row53_col2" class="data row53 col2" >$3.62</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row54" class="row_heading level0 row54" >Chanadar44</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row54_col0" class="data row54 col0" >$7.19</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row54_col1" class="data row54 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row54_col2" class="data row54 col2" >$3.59</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row55" class="row_heading level0 row55" >Saellyra72</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row55_col0" class="data row55 col0" >$7.18</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row55_col1" class="data row55 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row55_col2" class="data row55 col2" >$3.59</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row56" class="row_heading level0 row56" >Ryanara76</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row56_col0" class="data row56 col0" >$7.00</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row56_col1" class="data row56 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row56_col2" class="data row56 col2" >$3.50</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row57" class="row_heading level0 row57" >Yarolwen77</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row57_col0" class="data row57 col0" >$6.98</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row57_col1" class="data row57 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row57_col2" class="data row57 col2" >$3.49</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row58" class="row_heading level0 row58" >Hilaerin92</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row58_col0" class="data row58 col0" >$6.87</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row58_col1" class="data row58 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row58_col2" class="data row58 col2" >$3.44</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row59" class="row_heading level0 row59" >Aidain51</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row59_col0" class="data row59 col0" >$6.84</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row59_col1" class="data row59 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row59_col2" class="data row59 col2" >$3.42</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row60" class="row_heading level0 row60" >Qilatie51</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row60_col0" class="data row60 col0" >$6.81</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row60_col1" class="data row60 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row60_col2" class="data row60 col2" >$3.41</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row61" class="row_heading level0 row61" >Farusrian86</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row61_col0" class="data row61 col0" >$6.81</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row61_col1" class="data row61 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row61_col2" class="data row61 col2" >$3.41</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row62" class="row_heading level0 row62" >Lassast89</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row62_col0" class="data row62 col0" >$6.78</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row62_col1" class="data row62 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row62_col2" class="data row62 col2" >$3.39</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row63" class="row_heading level0 row63" >Raerithsti62</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row63_col0" class="data row63 col0" >$6.77</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row63_col1" class="data row63 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row63_col2" class="data row63 col2" >$3.38</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row64" class="row_heading level0 row64" >Chanosiaya39</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row64_col0" class="data row64 col0" >$6.75</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row64_col1" class="data row64 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row64_col2" class="data row64 col2" >$3.38</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row65" class="row_heading level0 row65" >Saida58</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row65_col0" class="data row65 col0" >$6.74</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row65_col1" class="data row65 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row65_col2" class="data row65 col2" >$3.37</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row66" class="row_heading level0 row66" >Lisosiast26</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row66_col0" class="data row66 col0" >$6.74</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row66_col1" class="data row66 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row66_col2" class="data row66 col2" >$3.37</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row67" class="row_heading level0 row67" >Chanosia60</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row67_col0" class="data row67 col0" >$6.74</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row67_col1" class="data row67 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row67_col2" class="data row67 col2" >$3.37</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row68" class="row_heading level0 row68" >Aeliriam77</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row68_col0" class="data row68 col0" >$6.72</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row68_col1" class="data row68 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row68_col2" class="data row68 col2" >$3.36</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row69" class="row_heading level0 row69" >Aduephos78</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row69_col0" class="data row69 col0" >$6.70</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row69_col1" class="data row69 col1" >3</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row69_col2" class="data row69 col2" >$2.23</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row70" class="row_heading level0 row70" >Iskosia51</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row70_col0" class="data row70 col0" >$6.70</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row70_col1" class="data row70 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row70_col2" class="data row70 col2" >$3.35</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row71" class="row_heading level0 row71" >Farenon57</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row71_col0" class="data row71 col0" >$6.64</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row71_col1" class="data row71 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row71_col2" class="data row71 col2" >$3.32</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row72" class="row_heading level0 row72" >Alaephos75</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row72_col0" class="data row72 col0" >$6.63</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row72_col1" class="data row72 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row72_col2" class="data row72 col2" >$3.31</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row73" class="row_heading level0 row73" >Assylla81</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row73_col0" class="data row73 col0" >$6.60</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row73_col1" class="data row73 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row73_col2" class="data row73 col2" >$3.30</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row74" class="row_heading level0 row74" >Aeri84</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row74_col0" class="data row74 col0" >$6.60</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row74_col1" class="data row74 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row74_col2" class="data row74 col2" >$3.30</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row75" class="row_heading level0 row75" >Lisassasta50</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row75_col0" class="data row75 col0" >$6.59</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row75_col1" class="data row75 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row75_col2" class="data row75 col2" >$3.29</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row76" class="row_heading level0 row76" >Marim28</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row76_col0" class="data row76 col0" >$6.56</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row76_col1" class="data row76 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row76_col2" class="data row76 col2" >$3.28</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row77" class="row_heading level0 row77" >Tyananurgue44</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row77_col0" class="data row77 col0" >$6.55</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row77_col1" class="data row77 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row77_col2" class="data row77 col2" >$3.28</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row78" class="row_heading level0 row78" >Ithergue48</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row78_col0" class="data row78 col0" >$6.42</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row78_col1" class="data row78 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row78_col2" class="data row78 col2" >$3.21</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row79" class="row_heading level0 row79" >Chanastst38</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row79_col0" class="data row79 col0" >$6.42</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row79_col1" class="data row79 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row79_col2" class="data row79 col2" >$3.21</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row80" class="row_heading level0 row80" >Lisasi93</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row80_col0" class="data row80 col0" >$6.42</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row80_col1" class="data row80 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row80_col2" class="data row80 col2" >$3.21</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row81" class="row_heading level0 row81" >Mindilsa60</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row81_col0" class="data row81 col0" >$6.37</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row81_col1" class="data row81 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row81_col2" class="data row81 col2" >$3.19</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row82" class="row_heading level0 row82" >Iaralrgue74</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row82_col0" class="data row82 col0" >$6.36</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row82_col1" class="data row82 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row82_col2" class="data row82 col2" >$3.18</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row83" class="row_heading level0 row83" >Sida61</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row83_col0" class="data row83 col0" >$6.34</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row83_col1" class="data row83 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row83_col2" class="data row83 col2" >$3.17</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row84" class="row_heading level0 row84" >Rinallorap73</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row84_col0" class="data row84 col0" >$6.32</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row84_col1" class="data row84 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row84_col2" class="data row84 col2" >$3.16</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row85" class="row_heading level0 row85" >Chadanto83</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row85_col0" class="data row85 col0" >$6.23</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row85_col1" class="data row85 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row85_col2" class="data row85 col2" >$3.12</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row86" class="row_heading level0 row86" >Marirrasta50</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row86_col0" class="data row86 col0" >$6.22</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row86_col1" class="data row86 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row86_col2" class="data row86 col2" >$3.11</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row87" class="row_heading level0 row87" >Iskossan49</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row87_col0" class="data row87 col0" >$6.18</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row87_col1" class="data row87 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row87_col2" class="data row87 col2" >$3.09</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row88" class="row_heading level0 row88" >Chamosia29</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row88_col0" class="data row88 col0" >$6.16</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row88_col1" class="data row88 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row88_col2" class="data row88 col2" >$3.08</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row89" class="row_heading level0 row89" >Filrion44</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row89_col0" class="data row89 col0" >$6.11</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row89_col1" class="data row89 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row89_col2" class="data row89 col2" >$3.06</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row90" class="row_heading level0 row90" >Lassassasda30</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row90_col0" class="data row90 col0" >$6.07</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row90_col1" class="data row90 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row90_col2" class="data row90 col2" >$3.04</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row91" class="row_heading level0 row91" >Eusur90</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row91_col0" class="data row91 col0" >$6.06</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row91_col1" class="data row91 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row91_col2" class="data row91 col2" >$3.03</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row92" class="row_heading level0 row92" >Raillydeu47</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row92_col0" class="data row92 col0" >$6.02</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row92_col1" class="data row92 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row92_col2" class="data row92 col2" >$3.01</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row93" class="row_heading level0 row93" >Saistyphos30</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row93_col0" class="data row93 col0" >$5.98</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row93_col1" class="data row93 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row93_col2" class="data row93 col2" >$2.99</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row94" class="row_heading level0 row94" >Tyaelistidru84</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row94_col0" class="data row94 col0" >$5.97</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row94_col1" class="data row94 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row94_col2" class="data row94 col2" >$2.98</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row95" class="row_heading level0 row95" >Pharithdil38</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row95_col0" class="data row95 col0" >$5.96</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row95_col1" class="data row95 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row95_col2" class="data row95 col2" >$2.98</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row96" class="row_heading level0 row96" >Lisossa63</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row96_col0" class="data row96 col0" >$5.92</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row96_col1" class="data row96 col1" >3</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row96_col2" class="data row96 col2" >$1.97</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row97" class="row_heading level0 row97" >Chanosiast43</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row97_col0" class="data row97 col0" >$5.92</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row97_col1" class="data row97 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row97_col2" class="data row97 col2" >$2.96</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row98" class="row_heading level0 row98" >Hailaphos89</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row98_col0" class="data row98 col0" >$5.87</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row98_col1" class="data row98 col1" >4</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row98_col2" class="data row98 col2" >$1.47</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row99" class="row_heading level0 row99" >Eosur70</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row99_col0" class="data row99 col0" >$5.85</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row99_col1" class="data row99 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row99_col2" class="data row99 col2" >$2.92</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row100" class="row_heading level0 row100" >Iskimnya76</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row100_col0" class="data row100 col0" >$5.82</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row100_col1" class="data row100 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row100_col2" class="data row100 col2" >$2.91</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row101" class="row_heading level0 row101" >Sundaststa26</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row101_col0" class="data row101 col0" >$5.80</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row101_col1" class="data row101 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row101_col2" class="data row101 col2" >$2.90</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row102" class="row_heading level0 row102" >Aeduera68</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row102_col0" class="data row102 col0" >$5.80</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row102_col1" class="data row102 col1" >3</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row102_col2" class="data row102 col2" >$1.93</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row103" class="row_heading level0 row103" >Lisirra55</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row103_col0" class="data row103 col0" >$5.79</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row103_col1" class="data row103 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row103_col2" class="data row103 col2" >$2.90</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row104" class="row_heading level0 row104" >Ethruard50</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row104_col0" class="data row104 col0" >$5.70</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row104_col1" class="data row104 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row104_col2" class="data row104 col2" >$2.85</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row105" class="row_heading level0 row105" >Chamadar61</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row105_col0" class="data row105 col0" >$5.67</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row105_col1" class="data row105 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row105_col2" class="data row105 col2" >$2.83</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row106" class="row_heading level0 row106" >Chamilsan75</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row106_col0" class="data row106 col0" >$5.64</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row106_col1" class="data row106 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row106_col2" class="data row106 col2" >$2.82</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row107" class="row_heading level0 row107" >Tyirithnu40</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row107_col0" class="data row107 col0" >$5.61</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row107_col1" class="data row107 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row107_col2" class="data row107 col2" >$2.81</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row108" class="row_heading level0 row108" >Assassa38</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row108_col0" class="data row108 col0" >$5.61</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row108_col1" class="data row108 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row108_col2" class="data row108 col2" >$2.80</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row109" class="row_heading level0 row109" >Eurallo89</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row109_col0" class="data row109 col0" >$5.60</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row109_col1" class="data row109 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row109_col2" class="data row109 col2" >$2.80</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row110" class="row_heading level0 row110" >Sausosia74</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row110_col0" class="data row110 col0" >$5.59</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row110_col1" class="data row110 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row110_col2" class="data row110 col2" >$2.79</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row111" class="row_heading level0 row111" >Liri91</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row111_col0" class="data row111 col0" >$5.59</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row111_col1" class="data row111 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row111_col2" class="data row111 col2" >$2.79</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row112" class="row_heading level0 row112" >Chanirrala39</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row112_col0" class="data row112 col0" >$5.56</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row112_col1" class="data row112 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row112_col2" class="data row112 col2" >$2.78</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row113" class="row_heading level0 row113" >Seosri62</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row113_col0" class="data row113 col0" >$5.53</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row113_col1" class="data row113 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row113_col2" class="data row113 col2" >$2.76</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row114" class="row_heading level0 row114" >Chamilsala65</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row114_col0" class="data row114 col0" >$5.52</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row114_col1" class="data row114 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row114_col2" class="data row114 col2" >$2.76</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row115" class="row_heading level0 row115" >Tyaelo67</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row115_col0" class="data row115 col0" >$5.48</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row115_col1" class="data row115 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row115_col2" class="data row115 col2" >$2.74</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row116" class="row_heading level0 row116" >Raesty92</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row116_col0" class="data row116 col0" >$5.46</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row116_col1" class="data row116 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row116_col2" class="data row116 col2" >$2.73</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row117" class="row_heading level0 row117" >Iskossa88</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row117_col0" class="data row117 col0" >$5.45</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row117_col1" class="data row117 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row117_col2" class="data row117 col2" >$2.72</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row118" class="row_heading level0 row118" >Queusurra38</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row118_col0" class="data row118 col0" >$5.40</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row118_col1" class="data row118 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row118_col2" class="data row118 col2" >$2.70</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row119" class="row_heading level0 row119" >Tyeosri53</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row119_col0" class="data row119 col0" >$5.21</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row119_col1" class="data row119 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row119_col2" class="data row119 col2" >$2.60</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row120" class="row_heading level0 row120" >Raesursurap33</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row120_col0" class="data row120 col0" >$5.20</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row120_col1" class="data row120 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row120_col2" class="data row120 col2" >$2.60</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row121" class="row_heading level0 row121" >Lisovynya38</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row121_col0" class="data row121 col0" >$5.15</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row121_col1" class="data row121 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row121_col2" class="data row121 col2" >$2.58</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row122" class="row_heading level0 row122" >Lassassast73</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row122_col0" class="data row122 col0" >$5.11</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row122_col1" class="data row122 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row122_col2" class="data row122 col2" >$2.55</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row123" class="row_heading level0 row123" >Iskista88</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row123_col0" class="data row123 col0" >$5.07</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row123_col1" class="data row123 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row123_col2" class="data row123 col2" >$2.54</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row124" class="row_heading level0 row124" >Aelalis34</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row124_col0" class="data row124 col0" >$5.06</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row124_col1" class="data row124 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row124_col2" class="data row124 col2" >$2.53</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row125" class="row_heading level0 row125" >Streural92</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row125_col0" class="data row125 col0" >$5.06</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row125_col1" class="data row125 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row125_col2" class="data row125 col2" >$2.53</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row126" class="row_heading level0 row126" >Thryallym62</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row126_col0" class="data row126 col0" >$5.00</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row126_col1" class="data row126 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row126_col2" class="data row126 col2" >$2.50</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row127" class="row_heading level0 row127" >Frichaststa61</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row127_col0" class="data row127 col0" >$4.95</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row127_col1" class="data row127 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row127_col2" class="data row127 col2" >$4.95</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row128" class="row_heading level0 row128" >Palurrian69</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row128_col0" class="data row128 col0" >$4.95</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row128_col1" class="data row128 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row128_col2" class="data row128 col2" >$4.95</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row129" class="row_heading level0 row129" >Tyarithn67</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row129_col0" class="data row129 col0" >$4.95</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row129_col1" class="data row129 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row129_col2" class="data row129 col2" >$4.95</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row130" class="row_heading level0 row130" >Qiluard68</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row130_col0" class="data row130 col0" >$4.95</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row130_col1" class="data row130 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row130_col2" class="data row130 col2" >$4.95</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row131" class="row_heading level0 row131" >Assossa43</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row131_col0" class="data row131 col0" >$4.89</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row131_col1" class="data row131 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row131_col2" class="data row131 col2" >$4.89</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row132" class="row_heading level0 row132" >Syathe73</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row132_col0" class="data row132 col0" >$4.89</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row132_col1" class="data row132 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row132_col2" class="data row132 col2" >$4.89</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row133" class="row_heading level0 row133" >Iathenudil29</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row133_col0" class="data row133 col0" >$4.88</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row133_col1" class="data row133 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row133_col2" class="data row133 col2" >$2.44</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row134" class="row_heading level0 row134" >Hiasur92</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row134_col0" class="data row134 col0" >$4.87</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row134_col1" class="data row134 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row134_col2" class="data row134 col2" >$4.87</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row135" class="row_heading level0 row135" >Ilophos58</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row135_col0" class="data row135 col0" >$4.87</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row135_col1" class="data row135 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row135_col2" class="data row135 col2" >$4.87</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row136" class="row_heading level0 row136" >Idaria87</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row136_col0" class="data row136 col0" >$4.87</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row136_col1" class="data row136 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row136_col2" class="data row136 col2" >$4.87</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row137" class="row_heading level0 row137" >Iasur80</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row137_col0" class="data row137 col0" >$4.87</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row137_col1" class="data row137 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row137_col2" class="data row137 col2" >$4.87</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row138" class="row_heading level0 row138" >Anallorgue57</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row138_col0" class="data row138 col0" >$4.87</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row138_col1" class="data row138 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row138_col2" class="data row138 col2" >$4.87</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row139" class="row_heading level0 row139" >Iskista96</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row139_col0" class="data row139 col0" >$4.83</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row139_col1" class="data row139 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row139_col2" class="data row139 col2" >$4.83</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row140" class="row_heading level0 row140" >Chamirraya83</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row140_col0" class="data row140 col0" >$4.83</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row140_col1" class="data row140 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row140_col2" class="data row140 col2" >$2.42</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row141" class="row_heading level0 row141" >Tyeuladeu30</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row141_col0" class="data row141 col0" >$4.82</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row141_col1" class="data row141 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row141_col2" class="data row141 col2" >$4.82</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row142" class="row_heading level0 row142" >Heosrisuir72</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row142_col0" class="data row142 col0" >$4.82</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row142_col1" class="data row142 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row142_col2" class="data row142 col2" >$4.82</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row143" class="row_heading level0 row143" >Sweecossa42</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row143_col0" class="data row143 col0" >$4.81</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row143_col1" class="data row143 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row143_col2" class="data row143 col2" >$2.41</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row144" class="row_heading level0 row144" >Yarithsurgue62</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row144_col0" class="data row144 col0" >$4.81</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row144_col1" class="data row144 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row144_col2" class="data row144 col2" >$2.41</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row145" class="row_heading level0 row145" >Lassjask63</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row145_col0" class="data row145 col0" >$4.80</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row145_col1" class="data row145 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row145_col2" class="data row145 col2" >$2.40</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row146" class="row_heading level0 row146" >Phenastya51</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row146_col0" class="data row146 col0" >$4.75</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row146_col1" class="data row146 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row146_col2" class="data row146 col2" >$4.75</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row147" class="row_heading level0 row147" >Irithrap69</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row147_col0" class="data row147 col0" >$4.75</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row147_col1" class="data row147 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row147_col2" class="data row147 col2" >$4.75</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row148" class="row_heading level0 row148" >Marilsa48</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row148_col0" class="data row148 col0" >$4.75</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row148_col1" class="data row148 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row148_col2" class="data row148 col2" >$4.75</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row149" class="row_heading level0 row149" >Eustyria89</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row149_col0" class="data row149 col0" >$4.75</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row149_col1" class="data row149 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row149_col2" class="data row149 col2" >$4.75</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row150" class="row_heading level0 row150" >Assastnya25</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row150_col0" class="data row150 col0" >$4.75</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row150_col1" class="data row150 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row150_col2" class="data row150 col2" >$2.38</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row151" class="row_heading level0 row151" >Quarunarn52</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row151_col0" class="data row151 col0" >$4.75</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row151_col1" class="data row151 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row151_col2" class="data row151 col2" >$4.75</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row152" class="row_heading level0 row152" >Heuralsti66</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row152_col0" class="data row152 col0" >$4.75</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row152_col1" class="data row152 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row152_col2" class="data row152 col2" >$4.75</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row153" class="row_heading level0 row153" >Riralsti91</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row153_col0" class="data row153 col0" >$4.67</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row153_col1" class="data row153 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row153_col2" class="data row153 col2" >$4.67</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row154" class="row_heading level0 row154" >Iskichinya81</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row154_col0" class="data row154 col0" >$4.67</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row154_col1" class="data row154 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row154_col2" class="data row154 col2" >$4.67</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row155" class="row_heading level0 row155" >Aesur96</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row155_col0" class="data row155 col0" >$4.66</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row155_col1" class="data row155 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row155_col2" class="data row155 col2" >$4.66</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row156" class="row_heading level0 row156" >Minduli80</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row156_col0" class="data row156 col0" >$4.62</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row156_col1" class="data row156 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row156_col2" class="data row156 col2" >$4.62</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row157" class="row_heading level0 row157" >Sondim68</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row157_col0" class="data row157 col0" >$4.62</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row157_col1" class="data row157 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row157_col2" class="data row157 col2" >$4.62</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row158" class="row_heading level0 row158" >Lirtossa84</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row158_col0" class="data row158 col0" >$4.62</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row158_col1" class="data row158 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row158_col2" class="data row158 col2" >$4.62</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row159" class="row_heading level0 row159" >Undjaskla97</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row159_col0" class="data row159 col0" >$4.57</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row159_col1" class="data row159 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row159_col2" class="data row159 col2" >$4.57</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row160" class="row_heading level0 row160" >Saelaephos52</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row160_col0" class="data row160 col0" >$4.56</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row160_col1" class="data row160 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row160_col2" class="data row160 col2" >$4.56</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row161" class="row_heading level0 row161" >Frichim27</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row161_col0" class="data row161 col0" >$4.56</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row161_col1" class="data row161 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row161_col2" class="data row161 col2" >$4.56</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row162" class="row_heading level0 row162" >Ina92</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row162_col0" class="data row162 col0" >$4.54</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row162_col1" class="data row162 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row162_col2" class="data row162 col2" >$4.54</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row163" class="row_heading level0 row163" >Undjasksya56</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row163_col0" class="data row163 col0" >$4.53</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row163_col1" class="data row163 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row163_col2" class="data row163 col2" >$4.53</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row164" class="row_heading level0 row164" >Dyally87</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row164_col0" class="data row164 col0" >$4.51</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row164_col1" class="data row164 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row164_col2" class="data row164 col2" >$4.51</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row165" class="row_heading level0 row165" >Tyisur83</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row165_col0" class="data row165 col0" >$4.51</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row165_col1" class="data row165 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row165_col2" class="data row165 col2" >$4.51</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row166" class="row_heading level0 row166" >Syalollorap93</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row166_col0" class="data row166 col0" >$4.51</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row166_col1" class="data row166 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row166_col2" class="data row166 col2" >$4.51</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row167" class="row_heading level0 row167" >Raysistast71</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row167_col0" class="data row167 col0" >$4.51</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row167_col1" class="data row167 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row167_col2" class="data row167 col2" >$4.51</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row168" class="row_heading level0 row168" >Iadueria43</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row168_col0" class="data row168 col0" >$4.50</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row168_col1" class="data row168 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row168_col2" class="data row168 col2" >$2.25</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row169" class="row_heading level0 row169" >Chamistast30</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row169_col0" class="data row169 col0" >$4.49</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row169_col1" class="data row169 col1" >3</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row169_col2" class="data row169 col2" >$1.50</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row170" class="row_heading level0 row170" >Stryanastip77</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row170_col0" class="data row170 col0" >$4.46</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row170_col1" class="data row170 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row170_col2" class="data row170 col2" >$2.23</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row171" class="row_heading level0 row171" >Leyirra83</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row171_col0" class="data row171 col0" >$4.45</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row171_col1" class="data row171 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row171_col2" class="data row171 col2" >$4.45</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row172" class="row_heading level0 row172" >Qarrian82</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row172_col0" class="data row172 col0" >$4.45</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row172_col1" class="data row172 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row172_col2" class="data row172 col2" >$4.45</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row173" class="row_heading level0 row173" >Lassilsa41</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row173_col0" class="data row173 col0" >$4.42</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row173_col1" class="data row173 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row173_col2" class="data row173 col2" >$2.21</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row174" class="row_heading level0 row174" >Sundast29</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row174_col0" class="data row174 col0" >$4.42</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row174_col1" class="data row174 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row174_col2" class="data row174 col2" >$2.21</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row175" class="row_heading level0 row175" >Taeduenu92</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row175_col0" class="data row175 col0" >$4.39</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row175_col1" class="data row175 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row175_col2" class="data row175 col2" >$4.39</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row176" class="row_heading level0 row176" >Ethralista69</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row176_col0" class="data row176 col0" >$4.39</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row176_col1" class="data row176 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row176_col2" class="data row176 col2" >$4.39</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row177" class="row_heading level0 row177" >Lamon28</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row177_col0" class="data row177 col0" >$4.39</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row177_col1" class="data row177 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row177_col2" class="data row177 col2" >$4.39</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row178" class="row_heading level0 row178" >Eurith26</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row178_col0" class="data row178 col0" >$4.37</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row178_col1" class="data row178 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row178_col2" class="data row178 col2" >$4.37</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row179" class="row_heading level0 row179" >Marassanya92</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row179_col0" class="data row179 col0" >$4.37</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row179_col1" class="data row179 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row179_col2" class="data row179 col2" >$4.37</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row180" class="row_heading level0 row180" >Lirtista72</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row180_col0" class="data row180 col0" >$4.36</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row180_col1" class="data row180 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row180_col2" class="data row180 col2" >$4.36</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row181" class="row_heading level0 row181" >Isrirgue68</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row181_col0" class="data row181 col0" >$4.36</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row181_col1" class="data row181 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row181_col2" class="data row181 col2" >$4.36</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row182" class="row_heading level0 row182" >Quelatarn54</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row182_col0" class="data row182 col0" >$4.33</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row182_col1" class="data row182 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row182_col2" class="data row182 col2" >$4.33</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row183" class="row_heading level0 row183" >Aellyria80</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row183_col0" class="data row183 col0" >$4.32</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row183_col1" class="data row183 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row183_col2" class="data row183 col2" >$4.32</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row184" class="row_heading level0 row184" >Irillo49</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row184_col0" class="data row184 col0" >$4.32</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row184_col1" class="data row184 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row184_col2" class="data row184 col2" >$4.32</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row185" class="row_heading level0 row185" >Idairin80</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row185_col0" class="data row185 col0" >$4.30</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row185_col1" class="data row185 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row185_col2" class="data row185 col2" >$4.30</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row186" class="row_heading level0 row186" >Chamadar79</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row186_col0" class="data row186 col0" >$4.30</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row186_col1" class="data row186 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row186_col2" class="data row186 col2" >$4.30</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row187" class="row_heading level0 row187" >Sundadarla27</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row187_col0" class="data row187 col0" >$4.30</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row187_col1" class="data row187 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row187_col2" class="data row187 col2" >$4.30</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row188" class="row_heading level0 row188" >Chamadarnya73</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row188_col0" class="data row188 col0" >$4.30</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row188_col1" class="data row188 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row188_col2" class="data row188 col2" >$4.30</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row189" class="row_heading level0 row189" >Lisassa26</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row189_col0" class="data row189 col0" >$4.25</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row189_col1" class="data row189 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row189_col2" class="data row189 col2" >$4.25</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row190" class="row_heading level0 row190" >Thourdirra92</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row190_col0" class="data row190 col0" >$4.25</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row190_col1" class="data row190 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row190_col2" class="data row190 col2" >$4.25</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row191" class="row_heading level0 row191" >Aeral85</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row191_col0" class="data row191 col0" >$4.25</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row191_col1" class="data row191 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row191_col2" class="data row191 col2" >$4.25</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row192" class="row_heading level0 row192" >Euna48</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row192_col0" class="data row192 col0" >$4.25</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row192_col1" class="data row192 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row192_col2" class="data row192 col2" >$4.25</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row193" class="row_heading level0 row193" >Eoralphos86</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row193_col0" class="data row193 col0" >$4.25</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row193_col1" class="data row193 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row193_col2" class="data row193 col2" >$2.12</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row194" class="row_heading level0 row194" >Chamadar27</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row194_col0" class="data row194 col0" >$4.23</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row194_col1" class="data row194 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row194_col2" class="data row194 col2" >$4.23</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row195" class="row_heading level0 row195" >Phaeduesurgue38</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row195_col0" class="data row195 col0" >$4.23</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row195_col1" class="data row195 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row195_col2" class="data row195 col2" >$4.23</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row196" class="row_heading level0 row196" >Ilariarin45</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row196_col0" class="data row196 col0" >$4.23</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row196_col1" class="data row196 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row196_col2" class="data row196 col2" >$4.23</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row197" class="row_heading level0 row197" >Frichadar89</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row197_col0" class="data row197 col0" >$4.23</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row197_col1" class="data row197 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row197_col2" class="data row197 col2" >$4.23</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row198" class="row_heading level0 row198" >Yaralnura48</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row198_col0" class="data row198 col0" >$4.19</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row198_col1" class="data row198 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row198_col2" class="data row198 col2" >$2.10</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row199" class="row_heading level0 row199" >Frichistasta59</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row199_col0" class="data row199 col0" >$4.17</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row199_col1" class="data row199 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row199_col2" class="data row199 col2" >$2.08</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row200" class="row_heading level0 row200" >Layjask75</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row200_col0" class="data row200 col0" >$4.16</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row200_col1" class="data row200 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row200_col2" class="data row200 col2" >$4.16</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row201" class="row_heading level0 row201" >Ralaeriadeu65</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row201_col0" class="data row201 col0" >$4.16</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row201_col1" class="data row201 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row201_col2" class="data row201 col2" >$4.16</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row202" class="row_heading level0 row202" >Isurriarap71</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row202_col0" class="data row202 col0" >$4.16</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row202_col1" class="data row202 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row202_col2" class="data row202 col2" >$4.16</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row203" class="row_heading level0 row203" >Marilsanya48</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row203_col0" class="data row203 col0" >$4.16</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row203_col1" class="data row203 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row203_col2" class="data row203 col2" >$4.16</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row204" class="row_heading level0 row204" >Assistasda90</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row204_col0" class="data row204 col0" >$4.15</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row204_col1" class="data row204 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row204_col2" class="data row204 col2" >$4.15</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row205" class="row_heading level0 row205" >Undirra73</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row205_col0" class="data row205 col0" >$4.15</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row205_col1" class="data row205 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row205_col2" class="data row205 col2" >$4.15</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row206" class="row_heading level0 row206" >Sirira97</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row206_col0" class="data row206 col0" >$4.15</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row206_col1" class="data row206 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row206_col2" class="data row206 col2" >$4.15</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row207" class="row_heading level0 row207" >Alallo58</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row207_col0" class="data row207 col0" >$4.14</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row207_col1" class="data row207 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row207_col2" class="data row207 col2" >$4.14</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row208" class="row_heading level0 row208" >Ralasti48</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row208_col0" class="data row208 col0" >$4.14</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row208_col1" class="data row208 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row208_col2" class="data row208 col2" >$4.14</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row209" class="row_heading level0 row209" >Sondadar26</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row209_col0" class="data row209 col0" >$4.14</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row209_col1" class="data row209 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row209_col2" class="data row209 col2" >$4.14</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row210" class="row_heading level0 row210" >Iskistasda86</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row210_col0" class="data row210 col0" >$4.14</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row210_col1" class="data row210 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row210_col2" class="data row210 col2" >$4.14</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row211" class="row_heading level0 row211" >Chamim85</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row211_col0" class="data row211 col0" >$4.12</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row211_col1" class="data row211 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row211_col2" class="data row211 col2" >$4.12</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row212" class="row_heading level0 row212" >Saistydru69</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row212_col0" class="data row212 col0" >$4.12</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row212_col1" class="data row212 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row212_col2" class="data row212 col2" >$4.12</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row213" class="row_heading level0 row213" >Lisirraya76</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row213_col0" class="data row213 col0" >$4.10</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row213_col1" class="data row213 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row213_col2" class="data row213 col2" >$4.10</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row214" class="row_heading level0 row214" >Ialo60</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row214_col0" class="data row214 col0" >$4.08</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row214_col1" class="data row214 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row214_col2" class="data row214 col2" >$4.08</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row215" class="row_heading level0 row215" >Whaestysu86</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row215_col0" class="data row215 col0" >$4.08</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row215_col1" class="data row215 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row215_col2" class="data row215 col2" >$4.08</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row216" class="row_heading level0 row216" >Marundi65</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row216_col0" class="data row216 col0" >$4.07</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row216_col1" class="data row216 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row216_col2" class="data row216 col2" >$4.07</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row217" class="row_heading level0 row217" >Reolacal36</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row217_col0" class="data row217 col0" >$4.07</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row217_col1" class="data row217 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row217_col2" class="data row217 col2" >$4.07</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row218" class="row_heading level0 row218" >Reulae52</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row218_col0" class="data row218 col0" >$4.07</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row218_col1" class="data row218 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row218_col2" class="data row218 col2" >$4.07</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row219" class="row_heading level0 row219" >Lirtilsan89</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row219_col0" class="data row219 col0" >$4.07</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row219_col1" class="data row219 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row219_col2" class="data row219 col2" >$4.07</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row220" class="row_heading level0 row220" >Lisjasksda68</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row220_col0" class="data row220 col0" >$4.05</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row220_col1" class="data row220 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row220_col2" class="data row220 col2" >$2.02</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row221" class="row_heading level0 row221" >Asur53</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row221_col0" class="data row221 col0" >$4.04</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row221_col1" class="data row221 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row221_col2" class="data row221 col2" >$2.02</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row222" class="row_heading level0 row222" >Phairinum94</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row222_col0" class="data row222 col0" >$4.00</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row222_col1" class="data row222 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row222_col2" class="data row222 col2" >$4.00</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row223" class="row_heading level0 row223" >Chanosseya79</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row223_col0" class="data row223 col0" >$4.00</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row223_col1" class="data row223 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row223_col2" class="data row223 col2" >$4.00</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row224" class="row_heading level0 row224" >Aillycal84</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row224_col0" class="data row224 col0" >$4.00</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row224_col1" class="data row224 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row224_col2" class="data row224 col2" >$4.00</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row225" class="row_heading level0 row225" >Iri67</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row225_col0" class="data row225 col0" >$4.00</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row225_col1" class="data row225 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row225_col2" class="data row225 col2" >$4.00</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row226" class="row_heading level0 row226" >Syasriria69</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row226_col0" class="data row226 col0" >$3.98</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row226_col1" class="data row226 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row226_col2" class="data row226 col2" >$1.99</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row227" class="row_heading level0 row227" >Ralonurin90</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row227_col0" class="data row227 col0" >$3.96</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row227_col1" class="data row227 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row227_col2" class="data row227 col2" >$3.96</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row228" class="row_heading level0 row228" >Hiadanurin36</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row228_col0" class="data row228 col0" >$3.96</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row228_col1" class="data row228 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row228_col2" class="data row228 col2" >$3.96</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row229" class="row_heading level0 row229" >Smecherdi88</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row229_col0" class="data row229 col0" >$3.96</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row229_col1" class="data row229 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row229_col2" class="data row229 col2" >$3.96</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row230" class="row_heading level0 row230" >Inguard95</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row230_col0" class="data row230 col0" >$3.96</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row230_col1" class="data row230 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row230_col2" class="data row230 col2" >$3.96</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row231" class="row_heading level0 row231" >Frichim77</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row231_col0" class="data row231 col0" >$3.96</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row231_col1" class="data row231 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row231_col2" class="data row231 col2" >$3.96</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row232" class="row_heading level0 row232" >Jiskirran77</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row232_col0" class="data row232 col0" >$3.96</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row232_col1" class="data row232 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row232_col2" class="data row232 col2" >$3.96</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row233" class="row_heading level0 row233" >Seolollo93</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row233_col0" class="data row233 col0" >$3.91</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row233_col1" class="data row233 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row233_col2" class="data row233 col2" >$3.91</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row234" class="row_heading level0 row234" >Jiskimsda56</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row234_col0" class="data row234 col0" >$3.91</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row234_col1" class="data row234 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row234_col2" class="data row234 col2" >$3.91</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row235" class="row_heading level0 row235" >Styaduen40</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row235_col0" class="data row235 col0" >$3.91</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row235_col1" class="data row235 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row235_col2" class="data row235 col2" >$3.91</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row236" class="row_heading level0 row236" >Rasrirgue43</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row236_col0" class="data row236 col0" >$3.91</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row236_col1" class="data row236 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row236_col2" class="data row236 col2" >$3.91</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row237" class="row_heading level0 row237" >Undadar97</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row237_col0" class="data row237 col0" >$3.91</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row237_col1" class="data row237 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row237_col2" class="data row237 col2" >$3.91</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row238" class="row_heading level0 row238" >Lisistasya93</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row238_col0" class="data row238 col0" >$3.91</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row238_col1" class="data row238 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row238_col2" class="data row238 col2" >$3.91</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row239" class="row_heading level0 row239" >Iladarla40</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row239_col0" class="data row239 col0" >$3.91</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row239_col1" class="data row239 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row239_col2" class="data row239 col2" >$1.96</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row240" class="row_heading level0 row240" >Bartassaya73</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row240_col0" class="data row240 col0" >$3.91</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row240_col1" class="data row240 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row240_col2" class="data row240 col2" >$3.91</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row241" class="row_heading level0 row241" >Cosadar58</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row241_col0" class="data row241 col0" >$3.91</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row241_col1" class="data row241 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row241_col2" class="data row241 col2" >$3.91</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row242" class="row_heading level0 row242" >Undotesta33</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row242_col0" class="data row242 col0" >$3.90</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row242_col1" class="data row242 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row242_col2" class="data row242 col2" >$3.90</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row243" class="row_heading level0 row243" >Mindjasksya61</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row243_col0" class="data row243 col0" >$3.89</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row243_col1" class="data row243 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row243_col2" class="data row243 col2" >$3.89</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row244" class="row_heading level0 row244" >Assassa43</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row244_col0" class="data row244 col0" >$3.89</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row244_col1" class="data row244 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row244_col2" class="data row244 col2" >$3.89</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row245" class="row_heading level0 row245" >Assassasda84</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row245_col0" class="data row245 col0" >$3.89</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row245_col1" class="data row245 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row245_col2" class="data row245 col2" >$3.89</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row246" class="row_heading level0 row246" >Reuthelis39</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row246_col0" class="data row246 col0" >$3.87</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row246_col1" class="data row246 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row246_col2" class="data row246 col2" >$1.94</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row247" class="row_heading level0 row247" >Jiskassa76</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row247_col0" class="data row247 col0" >$3.83</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row247_col1" class="data row247 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row247_col2" class="data row247 col2" >$1.92</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row248" class="row_heading level0 row248" >Tyeosristi57</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row248_col0" class="data row248 col0" >$3.82</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row248_col1" class="data row248 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row248_col2" class="data row248 col2" >$3.82</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row249" class="row_heading level0 row249" >Seudaillorap38</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row249_col0" class="data row249 col0" >$3.82</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row249_col1" class="data row249 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row249_col2" class="data row249 col2" >$3.82</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row250" class="row_heading level0 row250" >Heunadil74</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row250_col0" class="data row250 col0" >$3.82</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row250_col1" class="data row250 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row250_col2" class="data row250 col2" >$3.82</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row251" class="row_heading level0 row251" >Meosridil82</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row251_col0" class="data row251 col0" >$3.82</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row251_col1" class="data row251 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row251_col2" class="data row251 col2" >$1.91</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row252" class="row_heading level0 row252" >Jiskilsa35</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row252_col0" class="data row252 col0" >$3.81</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row252_col1" class="data row252 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row252_col2" class="data row252 col2" >$3.81</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row253" class="row_heading level0 row253" >Raesurdil91</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row253_col0" class="data row253 col0" >$3.81</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row253_col1" class="data row253 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row253_col2" class="data row253 col2" >$3.81</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row254" class="row_heading level0 row254" >Iarithdil76</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row254_col0" class="data row254 col0" >$3.81</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row254_col1" class="data row254 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row254_col2" class="data row254 col2" >$3.81</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row255" class="row_heading level0 row255" >Chamjasknya65</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row255_col0" class="data row255 col0" >$3.80</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row255_col1" class="data row255 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row255_col2" class="data row255 col2" >$1.90</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row256" class="row_heading level0 row256" >Sondilsa40</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row256_col0" class="data row256 col0" >$3.80</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row256_col1" class="data row256 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row256_col2" class="data row256 col2" >$1.90</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row257" class="row_heading level0 row257" >Quanenrian83</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row257_col0" class="data row257 col0" >$3.79</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row257_col1" class="data row257 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row257_col2" class="data row257 col2" >$3.79</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row258" class="row_heading level0 row258" >Phistym51</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row258_col0" class="data row258 col0" >$3.79</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row258_col1" class="data row258 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row258_col2" class="data row258 col2" >$3.79</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row259" class="row_heading level0 row259" >Aithelis62</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row259_col0" class="data row259 col0" >$3.79</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row259_col1" class="data row259 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row259_col2" class="data row259 col2" >$3.79</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row260" class="row_heading level0 row260" >Lirtistasta79</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row260_col0" class="data row260 col0" >$3.76</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row260_col1" class="data row260 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row260_col2" class="data row260 col2" >$1.88</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row261" class="row_heading level0 row261" >Arithllorin55</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row261_col0" class="data row261 col0" >$3.74</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row261_col1" class="data row261 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row261_col2" class="data row261 col2" >$3.74</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row262" class="row_heading level0 row262" >Frichilsasya78</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row262_col0" class="data row262 col0" >$3.74</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row262_col1" class="data row262 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row262_col2" class="data row262 col2" >$3.74</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row263" class="row_heading level0 row263" >Isri59</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row263_col0" class="data row263 col0" >$3.74</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row263_col1" class="data row263 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row263_col2" class="data row263 col2" >$3.74</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row264" class="row_heading level0 row264" >Strithenu87</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row264_col0" class="data row264 col0" >$3.73</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row264_col1" class="data row264 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row264_col2" class="data row264 col2" >$3.73</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row265" class="row_heading level0 row265" >Aisurphos78</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row265_col0" class="data row265 col0" >$3.73</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row265_col1" class="data row265 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row265_col2" class="data row265 col2" >$3.73</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row266" class="row_heading level0 row266" >Eulaeria40</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row266_col0" class="data row266 col0" >$3.73</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row266_col1" class="data row266 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row266_col2" class="data row266 col2" >$3.73</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row267" class="row_heading level0 row267" >Iaralsuir44</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row267_col0" class="data row267 col0" >$3.73</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row267_col1" class="data row267 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row267_col2" class="data row267 col2" >$3.73</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row268" class="row_heading level0 row268" >Yaliru88</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row268_col0" class="data row268 col0" >$3.71</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row268_col1" class="data row268 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row268_col2" class="data row268 col2" >$3.71</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row269" class="row_heading level0 row269" >Ririp86</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row269_col0" class="data row269 col0" >$3.71</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row269_col1" class="data row269 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row269_col2" class="data row269 col2" >$3.71</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row270" class="row_heading level0 row270" >Zontibe81</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row270_col0" class="data row270 col0" >$3.71</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row270_col1" class="data row270 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row270_col2" class="data row270 col2" >$3.71</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row271" class="row_heading level0 row271" >Iskjaskst81</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row271_col0" class="data row271 col0" >$3.71</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row271_col1" class="data row271 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row271_col2" class="data row271 col2" >$3.71</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row272" class="row_heading level0 row272" >Iliel92</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row272_col0" class="data row272 col0" >$3.70</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row272_col1" class="data row272 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row272_col2" class="data row272 col2" >$3.70</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row273" class="row_heading level0 row273" >Chamastya76</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row273_col0" class="data row273 col0" >$3.70</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row273_col1" class="data row273 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row273_col2" class="data row273 col2" >$3.70</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row274" class="row_heading level0 row274" >Sundjask71</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row274_col0" class="data row274 col0" >$3.68</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row274_col1" class="data row274 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row274_col2" class="data row274 col2" >$3.68</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row275" class="row_heading level0 row275" >Saelollop56</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row275_col0" class="data row275 col0" >$3.68</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row275_col1" class="data row275 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row275_col2" class="data row275 col2" >$3.68</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row276" class="row_heading level0 row276" >Frichjaskan98</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row276_col0" class="data row276 col0" >$3.68</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row276_col1" class="data row276 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row276_col2" class="data row276 col2" >$3.68</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row277" class="row_heading level0 row277" >Sundim98</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row277_col0" class="data row277 col0" >$3.66</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row277_col1" class="data row277 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row277_col2" class="data row277 col2" >$3.66</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row278" class="row_heading level0 row278" >Jiskosiala43</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row278_col0" class="data row278 col0" >$3.66</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row278_col1" class="data row278 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row278_col2" class="data row278 col2" >$3.66</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row279" class="row_heading level0 row279" >Sondossa91</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row279_col0" class="data row279 col0" >$3.62</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row279_col1" class="data row279 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row279_col2" class="data row279 col2" >$3.62</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row280" class="row_heading level0 row280" >Eula35</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row280_col0" class="data row280 col0" >$3.62</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row280_col1" class="data row280 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row280_col2" class="data row280 col2" >$3.62</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row281" class="row_heading level0 row281" >Lisimsda29</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row281_col0" class="data row281 col0" >$3.62</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row281_col1" class="data row281 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row281_col2" class="data row281 col2" >$3.62</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row282" class="row_heading level0 row282" >Phaestycal84</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row282_col0" class="data row282 col0" >$3.62</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row282_col1" class="data row282 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row282_col2" class="data row282 col2" >$3.62</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row283" class="row_heading level0 row283" >Frichossast86</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row283_col0" class="data row283 col0" >$3.62</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row283_col1" class="data row283 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row283_col2" class="data row283 col2" >$3.62</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row284" class="row_heading level0 row284" >Aellysup38</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row284_col0" class="data row284 col0" >$3.61</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row284_col1" class="data row284 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row284_col2" class="data row284 col2" >$3.61</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row285" class="row_heading level0 row285" >Ilirrasda54</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row285_col0" class="data row285 col0" >$3.61</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row285_col1" class="data row285 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row285_col2" class="data row285 col2" >$3.61</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row286" class="row_heading level0 row286" >Alim85</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row286_col0" class="data row286 col0" >$3.61</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row286_col1" class="data row286 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row286_col2" class="data row286 col2" >$3.61</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row287" class="row_heading level0 row287" >Raithe71</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row287_col0" class="data row287 col0" >$3.61</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row287_col1" class="data row287 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row287_col2" class="data row287 col2" >$3.61</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row288" class="row_heading level0 row288" >Frichossast75</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row288_col0" class="data row288 col0" >$3.61</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row288_col1" class="data row288 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row288_col2" class="data row288 col2" >$3.61</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row289" class="row_heading level0 row289" >Assithasta65</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row289_col0" class="data row289 col0" >$3.61</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row289_col1" class="data row289 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row289_col2" class="data row289 col2" >$3.61</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row290" class="row_heading level0 row290" >Idai61</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row290_col0" class="data row290 col0" >$3.60</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row290_col1" class="data row290 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row290_col2" class="data row290 col2" >$1.80</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row291" class="row_heading level0 row291" >Airidil41</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row291_col0" class="data row291 col0" >$3.59</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row291_col1" class="data row291 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row291_col2" class="data row291 col2" >$3.59</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row292" class="row_heading level0 row292" >Sondilsa35</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row292_col0" class="data row292 col0" >$3.58</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row292_col1" class="data row292 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row292_col2" class="data row292 col2" >$3.58</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row293" class="row_heading level0 row293" >Assilsan72</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row293_col0" class="data row293 col0" >$3.58</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row293_col1" class="data row293 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row293_col2" class="data row293 col2" >$3.58</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row294" class="row_heading level0 row294" >Iral74</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row294_col0" class="data row294 col0" >$3.58</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row294_col1" class="data row294 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row294_col2" class="data row294 col2" >$3.58</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row295" class="row_heading level0 row295" >Lirtossa78</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row295_col0" class="data row295 col0" >$3.58</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row295_col1" class="data row295 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row295_col2" class="data row295 col2" >$1.79</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row296" class="row_heading level0 row296" >Syadaillo88</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row296_col0" class="data row296 col0" >$3.57</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row296_col1" class="data row296 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row296_col2" class="data row296 col2" >$3.57</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row297" class="row_heading level0 row297" >Airithrin43</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row297_col0" class="data row297 col0" >$3.57</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row297_col1" class="data row297 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row297_col2" class="data row297 col2" >$3.57</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row298" class="row_heading level0 row298" >Sondim73</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row298_col0" class="data row298 col0" >$3.57</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row298_col1" class="data row298 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row298_col2" class="data row298 col2" >$3.57</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row299" class="row_heading level0 row299" >Qaronon57</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row299_col0" class="data row299 col0" >$3.57</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row299_col1" class="data row299 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row299_col2" class="data row299 col2" >$3.57</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row300" class="row_heading level0 row300" >Frichistast39</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row300_col0" class="data row300 col0" >$3.56</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row300_col1" class="data row300 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row300_col2" class="data row300 col2" >$3.56</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row301" class="row_heading level0 row301" >Chamucosda93</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row301_col0" class="data row301 col0" >$3.56</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row301_col1" class="data row301 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row301_col2" class="data row301 col2" >$3.56</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row302" class="row_heading level0 row302" >Tyida79</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row302_col0" class="data row302 col0" >$3.56</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row302_col1" class="data row302 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row302_col2" class="data row302 col2" >$3.56</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row303" class="row_heading level0 row303" >Umuard36</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row303_col0" class="data row303 col0" >$3.55</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row303_col1" class="data row303 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row303_col2" class="data row303 col2" >$3.55</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row304" class="row_heading level0 row304" >Lirtast83</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row304_col0" class="data row304 col0" >$3.55</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row304_col1" class="data row304 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row304_col2" class="data row304 col2" >$3.55</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row305" class="row_heading level0 row305" >Eodailis27</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row305_col0" class="data row305 col0" >$3.55</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row305_col1" class="data row305 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row305_col2" class="data row305 col2" >$3.55</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row306" class="row_heading level0 row306" >Assistast50</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row306_col0" class="data row306 col0" >$3.55</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row306_col1" class="data row306 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row306_col2" class="data row306 col2" >$3.55</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row307" class="row_heading level0 row307" >Tyaeristi78</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row307_col0" class="data row307 col0" >$3.51</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row307_col1" class="data row307 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row307_col2" class="data row307 col2" >$1.75</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row308" class="row_heading level0 row308" >Lisiriya82</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row308_col0" class="data row308 col0" >$3.51</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row308_col1" class="data row308 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row308_col2" class="data row308 col2" >$3.51</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row309" class="row_heading level0 row309" >Rithe77</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row309_col0" class="data row309 col0" >$3.51</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row309_col1" class="data row309 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row309_col2" class="data row309 col2" >$1.75</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row310" class="row_heading level0 row310" >Eudasu82</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row310_col0" class="data row310 col0" >$3.51</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row310_col1" class="data row310 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row310_col2" class="data row310 col2" >$3.51</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row311" class="row_heading level0 row311" >Lirtossan50</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row311_col0" class="data row311 col0" >$3.51</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row311_col1" class="data row311 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row311_col2" class="data row311 col2" >$3.51</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row312" class="row_heading level0 row312" >Heuli25</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row312_col0" class="data row312 col0" >$3.48</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row312_col1" class="data row312 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row312_col2" class="data row312 col2" >$3.48</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row313" class="row_heading level0 row313" >Ilimya66</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row313_col0" class="data row313 col0" >$3.48</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row313_col1" class="data row313 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row313_col2" class="data row313 col2" >$3.48</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row314" class="row_heading level0 row314" >Palatyon26</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row314_col0" class="data row314 col0" >$3.47</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row314_col1" class="data row314 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row314_col2" class="data row314 col2" >$3.47</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row315" class="row_heading level0 row315" >Lisossa25</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row315_col0" class="data row315 col0" >$3.44</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row315_col1" class="data row315 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row315_col2" class="data row315 col2" >$1.72</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row316" class="row_heading level0 row316" >Lirtistanya48</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row316_col0" class="data row316 col0" >$3.42</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row316_col1" class="data row316 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row316_col2" class="data row316 col2" >$3.42</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row317" class="row_heading level0 row317" >Leulaesti78</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row317_col0" class="data row317 col0" >$3.42</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row317_col1" class="data row317 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row317_col2" class="data row317 col2" >$3.42</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row318" class="row_heading level0 row318" >Saena74</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row318_col0" class="data row318 col0" >$3.39</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row318_col1" class="data row318 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row318_col2" class="data row318 col2" >$3.39</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row319" class="row_heading level0 row319" >Iskosian40</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row319_col0" class="data row319 col0" >$3.39</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row319_col1" class="data row319 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row319_col2" class="data row319 col2" >$3.39</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row320" class="row_heading level0 row320" >Hainaria90</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row320_col0" class="data row320 col0" >$3.39</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row320_col1" class="data row320 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row320_col2" class="data row320 col2" >$3.39</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row321" class="row_heading level0 row321" >Sundosiasta28</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row321_col0" class="data row321 col0" >$3.39</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row321_col1" class="data row321 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row321_col2" class="data row321 col2" >$3.39</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row322" class="row_heading level0 row322" >Sundossast30</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row322_col0" class="data row322 col0" >$3.39</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row322_col1" class="data row322 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row322_col2" class="data row322 col2" >$3.39</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row323" class="row_heading level0 row323" >Saisrilis27</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row323_col0" class="data row323 col0" >$3.39</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row323_col1" class="data row323 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row323_col2" class="data row323 col2" >$3.39</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row324" class="row_heading level0 row324" >Chanjask65</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row324_col0" class="data row324 col0" >$3.39</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row324_col1" class="data row324 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row324_col2" class="data row324 col2" >$1.69</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row325" class="row_heading level0 row325" >Raelly43</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row325_col0" class="data row325 col0" >$3.37</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row325_col1" class="data row325 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row325_col2" class="data row325 col2" >$3.37</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row326" class="row_heading level0 row326" >Chanirrasta87</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row326_col0" class="data row326 col0" >$3.36</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row326_col1" class="data row326 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row326_col2" class="data row326 col2" >$1.68</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row327" class="row_heading level0 row327" >Eulidru49</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row327_col0" class="data row327 col0" >$3.33</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row327_col1" class="data row327 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row327_col2" class="data row327 col2" >$1.67</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row328" class="row_heading level0 row328" >Iduedru67</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row328_col0" class="data row328 col0" >$3.32</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row328_col1" class="data row328 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row328_col2" class="data row328 col2" >$3.32</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row329" class="row_heading level0 row329" >Crausirra42</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row329_col0" class="data row329 col0" >$3.29</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row329_col1" class="data row329 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row329_col2" class="data row329 col2" >$3.29</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row330" class="row_heading level0 row330" >Chamimla73</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row330_col0" class="data row330 col0" >$3.27</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row330_col1" class="data row330 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row330_col2" class="data row330 col2" >$3.27</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row331" class="row_heading level0 row331" >Aenasu69</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row331_col0" class="data row331 col0" >$3.27</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row331_col1" class="data row331 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row331_col2" class="data row331 col2" >$3.27</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row332" class="row_heading level0 row332" >Faralcil63</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row332_col0" class="data row332 col0" >$3.27</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row332_col1" class="data row332 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row332_col2" class="data row332 col2" >$3.27</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row333" class="row_heading level0 row333" >Liawista80</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row333_col0" class="data row333 col0" >$3.27</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row333_col1" class="data row333 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row333_col2" class="data row333 col2" >$3.27</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row334" class="row_heading level0 row334" >Eurinu48</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row334_col0" class="data row334 col0" >$3.25</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row334_col1" class="data row334 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row334_col2" class="data row334 col2" >$3.25</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row335" class="row_heading level0 row335" >Astydil38</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row335_col0" class="data row335 col0" >$3.21</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row335_col1" class="data row335 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row335_col2" class="data row335 col2" >$3.21</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row336" class="row_heading level0 row336" >Lassilsala30</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row336_col0" class="data row336 col0" >$3.21</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row336_col1" class="data row336 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row336_col2" class="data row336 col2" >$3.21</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row337" class="row_heading level0 row337" >Haerithp41</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row337_col0" class="data row337 col0" >$3.20</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row337_col1" class="data row337 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row337_col2" class="data row337 col2" >$3.20</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row338" class="row_heading level0 row338" >Aerithnucal56</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row338_col0" class="data row338 col0" >$3.18</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row338_col1" class="data row338 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row338_col2" class="data row338 col2" >$1.59</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row339" class="row_heading level0 row339" >Phadue96</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row339_col0" class="data row339 col0" >$3.15</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row339_col1" class="data row339 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row339_col2" class="data row339 col2" >$3.15</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row340" class="row_heading level0 row340" >Aellyrialis39</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row340_col0" class="data row340 col0" >$3.15</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row340_col1" class="data row340 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row340_col2" class="data row340 col2" >$3.15</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row341" class="row_heading level0 row341" >Tyeuduephos81</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row341_col0" class="data row341 col0" >$3.15</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row341_col1" class="data row341 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row341_col2" class="data row341 col2" >$3.15</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row342" class="row_heading level0 row342" >Ialallo29</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row342_col0" class="data row342 col0" >$3.15</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row342_col1" class="data row342 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row342_col2" class="data row342 col2" >$3.15</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row343" class="row_heading level0 row343" >Jeyciman68</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row343_col0" class="data row343 col0" >$3.15</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row343_col1" class="data row343 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row343_col2" class="data row343 col2" >$3.15</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row344" class="row_heading level0 row344" >Chanjaskan37</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row344_col0" class="data row344 col0" >$3.14</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row344_col1" class="data row344 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row344_col2" class="data row344 col2" >$3.14</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row345" class="row_heading level0 row345" >Aelin32</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row345_col0" class="data row345 col0" >$3.14</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row345_col1" class="data row345 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row345_col2" class="data row345 col2" >$3.14</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row346" class="row_heading level0 row346" >Yasurra52</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row346_col0" class="data row346 col0" >$3.14</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row346_col1" class="data row346 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row346_col2" class="data row346 col2" >$3.14</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row347" class="row_heading level0 row347" >Iskossaya95</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row347_col0" class="data row347 col0" >$3.13</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row347_col1" class="data row347 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row347_col2" class="data row347 col2" >$1.56</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row348" class="row_heading level0 row348" >Lisjaskya84</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row348_col0" class="data row348 col0" >$3.11</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row348_col1" class="data row348 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row348_col2" class="data row348 col2" >$3.11</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row349" class="row_heading level0 row349" >Silinu63</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row349_col0" class="data row349 col0" >$3.11</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row349_col1" class="data row349 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row349_col2" class="data row349 col2" >$3.11</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row350" class="row_heading level0 row350" >Undistasta86</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row350_col0" class="data row350 col0" >$3.02</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row350_col1" class="data row350 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row350_col2" class="data row350 col2" >$3.02</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row351" class="row_heading level0 row351" >Aina42</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row351_col0" class="data row351 col0" >$3.01</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row351_col1" class="data row351 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row351_col2" class="data row351 col2" >$3.01</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row352" class="row_heading level0 row352" >Malista67</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row352_col0" class="data row352 col0" >$3.01</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row352_col1" class="data row352 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row352_col2" class="data row352 col2" >$3.01</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row353" class="row_heading level0 row353" >Sundast87</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row353_col0" class="data row353 col0" >$3.01</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row353_col1" class="data row353 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row353_col2" class="data row353 col2" >$3.01</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row354" class="row_heading level0 row354" >Rathellorin54</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row354_col0" class="data row354 col0" >$2.99</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row354_col1" class="data row354 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row354_col2" class="data row354 col2" >$1.50</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row355" class="row_heading level0 row355" >Siathecal92</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row355_col0" class="data row355 col0" >$2.98</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row355_col1" class="data row355 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row355_col2" class="data row355 col2" >$2.98</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row356" class="row_heading level0 row356" >Qilanrion65</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row356_col0" class="data row356 col0" >$2.98</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row356_col1" class="data row356 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row356_col2" class="data row356 col2" >$2.98</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row357" class="row_heading level0 row357" >Siarithria38</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row357_col0" class="data row357 col0" >$2.97</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row357_col1" class="data row357 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row357_col2" class="data row357 col2" >$2.97</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row358" class="row_heading level0 row358" >Aethedru70</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row358_col0" class="data row358 col0" >$2.97</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row358_col1" class="data row358 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row358_col2" class="data row358 col2" >$2.97</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row359" class="row_heading level0 row359" >Chanirra79</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row359_col0" class="data row359 col0" >$2.97</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row359_col1" class="data row359 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row359_col2" class="data row359 col2" >$2.97</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row360" class="row_heading level0 row360" >Phainasu47</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row360_col0" class="data row360 col0" >$2.91</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row360_col1" class="data row360 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row360_col2" class="data row360 col2" >$2.91</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row361" class="row_heading level0 row361" >Chanjaskan89</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row361_col0" class="data row361 col0" >$2.91</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row361_col1" class="data row361 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row361_col2" class="data row361 col2" >$1.46</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row362" class="row_heading level0 row362" >Yarmol79</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row362_col0" class="data row362 col0" >$2.91</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row362_col1" class="data row362 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row362_col2" class="data row362 col2" >$2.91</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row363" class="row_heading level0 row363" >Jiskjask80</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row363_col0" class="data row363 col0" >$2.91</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row363_col1" class="data row363 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row363_col2" class="data row363 col2" >$2.91</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row364" class="row_heading level0 row364" >Eusri26</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row364_col0" class="data row364 col0" >$2.91</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row364_col1" class="data row364 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row364_col2" class="data row364 col2" >$2.91</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row365" class="row_heading level0 row365" >Phially37</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row365_col0" class="data row365 col0" >$2.88</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row365_col1" class="data row365 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row365_col2" class="data row365 col2" >$2.88</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row366" class="row_heading level0 row366" >Seuthelis34</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row366_col0" class="data row366 col0" >$2.88</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row366_col1" class="data row366 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row366_col2" class="data row366 col2" >$2.88</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row367" class="row_heading level0 row367" >Yarirarn35</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row367_col0" class="data row367 col0" >$2.88</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row367_col1" class="data row367 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row367_col2" class="data row367 col2" >$2.88</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row368" class="row_heading level0 row368" >Ingonon91</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row368_col0" class="data row368 col0" >$2.88</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row368_col1" class="data row368 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row368_col2" class="data row368 col2" >$2.88</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row369" class="row_heading level0 row369" >Tyidainu31</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row369_col0" class="data row369 col0" >$2.86</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row369_col1" class="data row369 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row369_col2" class="data row369 col2" >$2.86</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row370" class="row_heading level0 row370" >Billysu76</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row370_col0" class="data row370 col0" >$2.86</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row370_col1" class="data row370 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row370_col2" class="data row370 col2" >$2.86</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row371" class="row_heading level0 row371" >Frichassala85</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row371_col0" class="data row371 col0" >$2.85</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row371_col1" class="data row371 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row371_col2" class="data row371 col2" >$1.43</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row372" class="row_heading level0 row372" >Quarusrion32</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row372_col0" class="data row372 col0" >$2.83</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row372_col1" class="data row372 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row372_col2" class="data row372 col2" >$1.42</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row373" class="row_heading level0 row373" >Ilosu82</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row373_col0" class="data row373 col0" >$2.82</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row373_col1" class="data row373 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row373_col2" class="data row373 col2" >$2.82</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row374" class="row_heading level0 row374" >Assosiasta83</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row374_col0" class="data row374 col0" >$2.82</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row374_col1" class="data row374 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row374_col2" class="data row374 col2" >$2.82</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row375" class="row_heading level0 row375" >Ithesuphos68</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row375_col0" class="data row375 col0" >$2.78</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row375_col1" class="data row375 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row375_col2" class="data row375 col2" >$2.78</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row376" class="row_heading level0 row376" >Yasur35</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row376_col0" class="data row376 col0" >$2.78</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row376_col1" class="data row376 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row376_col2" class="data row376 col2" >$2.78</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row377" class="row_heading level0 row377" >Tyalaesu89</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row377_col0" class="data row377 col0" >$2.78</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row377_col1" class="data row377 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row377_col2" class="data row377 col2" >$2.78</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row378" class="row_heading level0 row378" >Phadai31</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row378_col0" class="data row378 col0" >$2.78</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row378_col1" class="data row378 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row378_col2" class="data row378 col2" >$2.78</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row379" class="row_heading level0 row379" >Sondenasta63</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row379_col0" class="data row379 col0" >$2.77</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row379_col1" class="data row379 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row379_col2" class="data row379 col2" >$2.77</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row380" class="row_heading level0 row380" >Baelollodeu94</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row380_col0" class="data row380 col0" >$2.77</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row380_col1" class="data row380 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row380_col2" class="data row380 col2" >$2.77</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row381" class="row_heading level0 row381" >Undiwinya88</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row381_col0" class="data row381 col0" >$2.77</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row381_col1" class="data row381 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row381_col2" class="data row381 col2" >$2.77</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row382" class="row_heading level0 row382" >Marassaya49</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row382_col0" class="data row382 col0" >$2.72</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row382_col1" class="data row382 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row382_col2" class="data row382 col2" >$2.72</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row383" class="row_heading level0 row383" >Mindadaran26</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row383_col0" class="data row383 col0" >$2.72</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row383_col1" class="data row383 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row383_col2" class="data row383 col2" >$2.72</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row384" class="row_heading level0 row384" >Aeral43</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row384_col0" class="data row384 col0" >$2.72</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row384_col1" class="data row384 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row384_col2" class="data row384 col2" >$2.72</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row385" class="row_heading level0 row385" >Alarap40</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row385_col0" class="data row385 col0" >$2.72</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row385_col1" class="data row385 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row385_col2" class="data row385 col2" >$2.72</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row386" class="row_heading level0 row386" >Sondassa48</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row386_col0" class="data row386 col0" >$2.67</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row386_col1" class="data row386 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row386_col2" class="data row386 col2" >$2.67</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row387" class="row_heading level0 row387" >Airal46</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row387_col0" class="data row387 col0" >$2.67</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row387_col1" class="data row387 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row387_col2" class="data row387 col2" >$2.67</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row388" class="row_heading level0 row388" >Seudanu38</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row388_col0" class="data row388 col0" >$2.67</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row388_col1" class="data row388 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row388_col2" class="data row388 col2" >$2.67</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row389" class="row_heading level0 row389" >Erudrion71</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row389_col0" class="data row389 col0" >$2.66</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row389_col1" class="data row389 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row389_col2" class="data row389 col2" >$1.33</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row390" class="row_heading level0 row390" >Aiduesu83</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row390_col0" class="data row390 col0" >$2.63</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row390_col1" class="data row390 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row390_col2" class="data row390 col2" >$2.63</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row391" class="row_heading level0 row391" >Tyithesura58</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row391_col0" class="data row391 col0" >$2.60</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row391_col1" class="data row391 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row391_col2" class="data row391 col2" >$2.60</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row392" class="row_heading level0 row392" >Eothe56</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row392_col0" class="data row392 col0" >$2.60</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row392_col1" class="data row392 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row392_col2" class="data row392 col2" >$2.60</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row393" class="row_heading level0 row393" >Yasrisu92</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row393_col0" class="data row393 col0" >$2.60</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row393_col1" class="data row393 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row393_col2" class="data row393 col2" >$2.60</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row394" class="row_heading level0 row394" >Eusri44</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row394_col0" class="data row394 col0" >$2.55</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row394_col1" class="data row394 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row394_col2" class="data row394 col2" >$2.55</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row395" class="row_heading level0 row395" >Saedaiphos46</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row395_col0" class="data row395 col0" >$2.55</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row395_col1" class="data row395 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row395_col2" class="data row395 col2" >$2.55</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row396" class="row_heading level0 row396" >Raedalis34</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row396_col0" class="data row396 col0" >$2.55</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row396_col1" class="data row396 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row396_col2" class="data row396 col2" >$2.55</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row397" class="row_heading level0 row397" >Zhisrisu83</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row397_col0" class="data row397 col0" >$2.46</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row397_col1" class="data row397 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row397_col2" class="data row397 col2" >$1.23</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row398" class="row_heading level0 row398" >Chadossa89</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row398_col0" class="data row398 col0" >$2.46</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row398_col1" class="data row398 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row398_col2" class="data row398 col2" >$2.46</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row399" class="row_heading level0 row399" >Undare39</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row399_col0" class="data row399 col0" >$2.46</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row399_col1" class="data row399 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row399_col2" class="data row399 col2" >$2.46</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row400" class="row_heading level0 row400" >Aina43</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row400_col0" class="data row400 col0" >$2.46</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row400_col1" class="data row400 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row400_col2" class="data row400 col2" >$2.46</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row401" class="row_heading level0 row401" >Aela49</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row401_col0" class="data row401 col0" >$2.46</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row401_col1" class="data row401 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row401_col2" class="data row401 col2" >$2.46</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row402" class="row_heading level0 row402" >Chamadarsda63</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row402_col0" class="data row402 col0" >$2.46</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row402_col1" class="data row402 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row402_col2" class="data row402 col2" >$2.46</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row403" class="row_heading level0 row403" >Adairialis76</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row403_col0" class="data row403 col0" >$2.46</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row403_col1" class="data row403 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row403_col2" class="data row403 col2" >$2.46</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row404" class="row_heading level0 row404" >Indirrian56</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row404_col0" class="data row404 col0" >$2.46</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row404_col1" class="data row404 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row404_col2" class="data row404 col2" >$2.46</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row405" class="row_heading level0 row405" >Quinarap53</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row405_col0" class="data row405 col0" >$2.46</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row405_col1" class="data row405 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row405_col2" class="data row405 col2" >$2.46</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row406" class="row_heading level0 row406" >Phaedai25</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row406_col0" class="data row406 col0" >$2.46</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row406_col1" class="data row406 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row406_col2" class="data row406 col2" >$2.46</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row407" class="row_heading level0 row407" >Fironon91</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row407_col0" class="data row407 col0" >$2.46</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row407_col1" class="data row407 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row407_col2" class="data row407 col2" >$2.46</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row408" class="row_heading level0 row408" >Yathecal82</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row408_col0" class="data row408 col0" >$2.41</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row408_col1" class="data row408 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row408_col2" class="data row408 col2" >$2.41</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row409" class="row_heading level0 row409" >Iskossasda43</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row409_col0" class="data row409 col0" >$2.41</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row409_col1" class="data row409 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row409_col2" class="data row409 col2" >$2.41</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row410" class="row_heading level0 row410" >Yalo71</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row410_col0" class="data row410 col0" >$2.41</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row410_col1" class="data row410 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row410_col2" class="data row410 col2" >$2.41</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row411" class="row_heading level0 row411" >Aerithriaphos45</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row411_col0" class="data row411 col0" >$2.38</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row411_col1" class="data row411 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row411_col2" class="data row411 col2" >$2.38</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row412" class="row_heading level0 row412" >Iskjaskan81</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row412_col0" class="data row412 col0" >$2.38</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row412_col1" class="data row412 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row412_col2" class="data row412 col2" >$2.38</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row413" class="row_heading level0 row413" >Siarinum43</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row413_col0" class="data row413 col0" >$2.38</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row413_col1" class="data row413 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row413_col2" class="data row413 col2" >$2.38</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row414" class="row_heading level0 row414" >Yalostiphos68</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row414_col0" class="data row414 col0" >$2.37</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row414_col1" class="data row414 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row414_col2" class="data row414 col2" >$2.37</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row415" class="row_heading level0 row415" >Eosrirgue62</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row415_col0" class="data row415 col0" >$2.36</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row415_col1" class="data row415 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row415_col2" class="data row415 col2" >$2.36</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row416" class="row_heading level0 row416" >Saerallora71</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row416_col0" class="data row416 col0" >$2.36</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row416_col1" class="data row416 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row416_col2" class="data row416 col2" >$2.36</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row417" class="row_heading level0 row417" >Tyaerith73</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row417_col0" class="data row417 col0" >$2.36</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row417_col1" class="data row417 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row417_col2" class="data row417 col2" >$2.36</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row418" class="row_heading level0 row418" >Chanosia65</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row418_col0" class="data row418 col0" >$2.36</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row418_col1" class="data row418 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row418_col2" class="data row418 col2" >$2.36</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row419" class="row_heading level0 row419" >Eullydru35</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row419_col0" class="data row419 col0" >$2.35</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row419_col1" class="data row419 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row419_col2" class="data row419 col2" >$2.35</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row420" class="row_heading level0 row420" >Yarithphos28</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row420_col0" class="data row420 col0" >$2.35</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row420_col1" class="data row420 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row420_col2" class="data row420 col2" >$2.35</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row421" class="row_heading level0 row421" >Aeral97</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row421_col0" class="data row421 col0" >$2.35</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row421_col1" class="data row421 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row421_col2" class="data row421 col2" >$2.35</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row422" class="row_heading level0 row422" >Undadarla37</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row422_col0" class="data row422 col0" >$2.35</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row422_col1" class="data row422 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row422_col2" class="data row422 col2" >$2.35</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row423" class="row_heading level0 row423" >Filon68</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row423_col0" class="data row423 col0" >$2.34</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row423_col1" class="data row423 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row423_col2" class="data row423 col2" >$2.34</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row424" class="row_heading level0 row424" >Iallyphos37</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row424_col0" class="data row424 col0" >$2.34</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row424_col1" class="data row424 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row424_col2" class="data row424 col2" >$2.34</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row425" class="row_heading level0 row425" >Lamil79</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row425_col0" class="data row425 col0" >$2.34</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row425_col1" class="data row425 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row425_col2" class="data row425 col2" >$2.34</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row426" class="row_heading level0 row426" >Irith83</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row426_col0" class="data row426 col0" >$2.33</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row426_col1" class="data row426 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row426_col2" class="data row426 col2" >$2.33</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row427" class="row_heading level0 row427" >Alaesu77</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row427_col0" class="data row427 col0" >$2.33</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row427_col1" class="data row427 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row427_col2" class="data row427 col2" >$2.33</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row428" class="row_heading level0 row428" >Aiduecal76</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row428_col0" class="data row428 col0" >$2.33</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row428_col1" class="data row428 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row428_col2" class="data row428 col2" >$2.33</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row429" class="row_heading level0 row429" >Hirirap39</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row429_col0" class="data row429 col0" >$2.33</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row429_col1" class="data row429 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row429_col2" class="data row429 col2" >$2.33</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row430" class="row_heading level0 row430" >Qilunan34</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row430_col0" class="data row430 col0" >$2.32</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row430_col1" class="data row430 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row430_col2" class="data row430 col2" >$2.32</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row431" class="row_heading level0 row431" >Eolo46</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row431_col0" class="data row431 col0" >$2.32</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row431_col1" class="data row431 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row431_col2" class="data row431 col2" >$2.32</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row432" class="row_heading level0 row432" >Aethe80</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row432_col0" class="data row432 col0" >$2.32</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row432_col1" class="data row432 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row432_col2" class="data row432 col2" >$2.32</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row433" class="row_heading level0 row433" >Lisadar44</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row433_col0" class="data row433 col0" >$2.31</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row433_col1" class="data row433 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row433_col2" class="data row433 col2" >$2.31</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row434" class="row_heading level0 row434" >Tyaelorgue39</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row434_col0" class="data row434 col0" >$2.31</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row434_col1" class="data row434 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row434_col2" class="data row434 col2" >$2.31</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row435" class="row_heading level0 row435" >Mindetosya30</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row435_col0" class="data row435 col0" >$2.31</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row435_col1" class="data row435 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row435_col2" class="data row435 col2" >$2.31</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row436" class="row_heading level0 row436" >Eratiel90</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row436_col0" class="data row436 col0" >$2.29</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row436_col1" class="data row436 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row436_col2" class="data row436 col2" >$2.29</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row437" class="row_heading level0 row437" >Iskirra45</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row437_col0" class="data row437 col0" >$2.29</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row437_col1" class="data row437 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row437_col2" class="data row437 col2" >$2.29</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row438" class="row_heading level0 row438" >Tyaelly53</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row438_col0" class="data row438 col0" >$2.29</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row438_col1" class="data row438 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row438_col2" class="data row438 col2" >$2.29</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row439" class="row_heading level0 row439" >Phyali88</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row439_col0" class="data row439 col0" >$2.29</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row439_col1" class="data row439 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row439_col2" class="data row439 col2" >$2.29</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row440" class="row_heading level0 row440" >Indonmol95</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row440_col0" class="data row440 col0" >$2.29</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row440_col1" class="data row440 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row440_col2" class="data row440 col2" >$2.29</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row441" class="row_heading level0 row441" >Ilaesudil92</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row441_col0" class="data row441 col0" >$2.28</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row441_col1" class="data row441 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row441_col2" class="data row441 col2" >$2.28</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row442" class="row_heading level0 row442" >Hiasri33</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row442_col0" class="data row442 col0" >$2.28</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row442_col1" class="data row442 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row442_col2" class="data row442 col2" >$2.28</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row443" class="row_heading level0 row443" >Undirrasta89</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row443_col0" class="data row443 col0" >$2.28</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row443_col1" class="data row443 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row443_col2" class="data row443 col2" >$2.28</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row444" class="row_heading level0 row444" >Eosursurap97</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row444_col0" class="data row444 col0" >$2.23</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row444_col1" class="data row444 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row444_col2" class="data row444 col2" >$2.23</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row445" class="row_heading level0 row445" >Lisossanya98</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row445_col0" class="data row445 col0" >$2.23</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row445_col1" class="data row445 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row445_col2" class="data row445 col2" >$2.23</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row446" class="row_heading level0 row446" >Inguron55</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row446_col0" class="data row446 col0" >$2.23</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row446_col1" class="data row446 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row446_col2" class="data row446 col2" >$2.23</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row447" class="row_heading level0 row447" >Nitherian58</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row447_col0" class="data row447 col0" >$2.23</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row447_col1" class="data row447 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row447_col2" class="data row447 col2" >$2.23</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row448" class="row_heading level0 row448" >Hiarideu73</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row448_col0" class="data row448 col0" >$2.23</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row448_col1" class="data row448 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row448_col2" class="data row448 col2" >$2.23</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row449" class="row_heading level0 row449" >Koikirra25</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row449_col0" class="data row449 col0" >$2.23</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row449_col1" class="data row449 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row449_col2" class="data row449 col2" >$2.23</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row450" class="row_heading level0 row450" >Syally44</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row450_col0" class="data row450 col0" >$2.22</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row450_col1" class="data row450 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row450_col2" class="data row450 col2" >$2.22</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row451" class="row_heading level0 row451" >Ilassa51</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row451_col0" class="data row451 col0" >$2.21</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row451_col1" class="data row451 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row451_col2" class="data row451 col2" >$2.21</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row452" class="row_heading level0 row452" >Strairisti57</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row452_col0" class="data row452 col0" >$2.21</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row452_col1" class="data row452 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row452_col2" class="data row452 col2" >$2.21</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row453" class="row_heading level0 row453" >Frichast72</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row453_col0" class="data row453 col0" >$2.20</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row453_col1" class="data row453 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row453_col2" class="data row453 col2" >$2.20</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row454" class="row_heading level0 row454" >Sundassa93</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row454_col0" class="data row454 col0" >$2.20</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row454_col1" class="data row454 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row454_col2" class="data row454 col2" >$2.20</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row455" class="row_heading level0 row455" >Yarithllodeu72</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row455_col0" class="data row455 col0" >$2.19</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row455_col1" class="data row455 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row455_col2" class="data row455 col2" >$2.19</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row456" class="row_heading level0 row456" >Marjasksda39</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row456_col0" class="data row456 col0" >$2.19</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row456_col1" class="data row456 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row456_col2" class="data row456 col2" >$2.19</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row457" class="row_heading level0 row457" >Mindossasya74</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row457_col0" class="data row457 col0" >$2.17</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row457_col1" class="data row457 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row457_col2" class="data row457 col2" >$2.17</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row458" class="row_heading level0 row458" >Frichjask31</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row458_col0" class="data row458 col0" >$2.17</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row458_col1" class="data row458 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row458_col2" class="data row458 col2" >$2.17</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row459" class="row_heading level0 row459" >Sondimla25</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row459_col0" class="data row459 col0" >$2.17</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row459_col1" class="data row459 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row459_col2" class="data row459 col2" >$2.17</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row460" class="row_heading level0 row460" >Tyidue95</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row460_col0" class="data row460 col0" >$2.17</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row460_col1" class="data row460 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row460_col2" class="data row460 col2" >$2.17</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row461" class="row_heading level0 row461" >Lassimla92</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row461_col0" class="data row461 col0" >$2.17</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row461_col1" class="data row461 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row461_col2" class="data row461 col2" >$2.17</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row462" class="row_heading level0 row462" >Alo67</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row462_col0" class="data row462 col0" >$2.11</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row462_col1" class="data row462 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row462_col2" class="data row462 col2" >$2.11</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row463" class="row_heading level0 row463" >Lisista27</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row463_col0" class="data row463 col0" >$2.11</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row463_col1" class="data row463 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row463_col2" class="data row463 col2" >$2.11</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row464" class="row_heading level0 row464" >Lisassa49</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row464_col0" class="data row464 col0" >$2.11</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row464_col1" class="data row464 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row464_col2" class="data row464 col2" >$2.11</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row465" class="row_heading level0 row465" >Tauldilsa43</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row465_col0" class="data row465 col0" >$2.11</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row465_col1" class="data row465 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row465_col2" class="data row465 col2" >$2.11</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row466" class="row_heading level0 row466" >Eryon48</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row466_col0" class="data row466 col0" >$2.11</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row466_col1" class="data row466 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row466_col2" class="data row466 col2" >$2.11</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row467" class="row_heading level0 row467" >Lirtassa47</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row467_col0" class="data row467 col0" >$2.09</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row467_col1" class="data row467 col1" >2</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row467_col2" class="data row467 col2" >$1.04</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row468" class="row_heading level0 row468" >Mindassast27</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row468_col0" class="data row468 col0" >$2.07</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row468_col1" class="data row468 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row468_col2" class="data row468 col2" >$2.07</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row469" class="row_heading level0 row469" >Marilsasya33</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row469_col0" class="data row469 col0" >$2.07</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row469_col1" class="data row469 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row469_col2" class="data row469 col2" >$2.07</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row470" class="row_heading level0 row470" >Filrion59</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row470_col0" class="data row470 col0" >$2.07</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row470_col1" class="data row470 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row470_col2" class="data row470 col2" >$2.07</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row471" class="row_heading level0 row471" >Sidap51</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row471_col0" class="data row471 col0" >$2.07</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row471_col1" class="data row471 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row471_col2" class="data row471 col2" >$2.07</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row472" class="row_heading level0 row472" >Undast38</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row472_col0" class="data row472 col0" >$2.04</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row472_col1" class="data row472 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row472_col2" class="data row472 col2" >$2.04</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row473" class="row_heading level0 row473" >Euliria52</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row473_col0" class="data row473 col0" >$2.04</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row473_col1" class="data row473 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row473_col2" class="data row473 col2" >$2.04</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row474" class="row_heading level0 row474" >Wailin72</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row474_col0" class="data row474 col0" >$2.04</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row474_col1" class="data row474 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row474_col2" class="data row474 col2" >$2.04</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row475" class="row_heading level0 row475" >Aeliriarin93</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row475_col0" class="data row475 col0" >$2.04</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row475_col1" class="data row475 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row475_col2" class="data row475 col2" >$2.04</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row476" class="row_heading level0 row476" >Yasur85</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row476_col0" class="data row476 col0" >$2.04</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row476_col1" class="data row476 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row476_col2" class="data row476 col2" >$2.04</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row477" class="row_heading level0 row477" >Deelilsasya30</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row477_col0" class="data row477 col0" >$1.98</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row477_col1" class="data row477 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row477_col2" class="data row477 col2" >$1.98</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row478" class="row_heading level0 row478" >Rina82</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row478_col0" class="data row478 col0" >$1.98</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row478_col1" class="data row478 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row478_col2" class="data row478 col2" >$1.98</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row479" class="row_heading level0 row479" >Tyaenasti87</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row479_col0" class="data row479 col0" >$1.96</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row479_col1" class="data row479 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row479_col2" class="data row479 col2" >$1.96</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row480" class="row_heading level0 row480" >Yadacal26</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row480_col0" class="data row480 col0" >$1.93</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row480_col1" class="data row480 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row480_col2" class="data row480 col2" >$1.93</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row481" class="row_heading level0 row481" >Iarilis73</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row481_col0" class="data row481 col0" >$1.93</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row481_col1" class="data row481 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row481_col2" class="data row481 col2" >$1.93</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row482" class="row_heading level0 row482" >Assosia38</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row482_col0" class="data row482 col0" >$1.93</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row482_col1" class="data row482 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row482_col2" class="data row482 col2" >$1.93</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row483" class="row_heading level0 row483" >Shidai42</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row483_col0" class="data row483 col0" >$1.93</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row483_col1" class="data row483 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row483_col2" class="data row483 col2" >$1.93</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row484" class="row_heading level0 row484" >Ennoncil86</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row484_col0" class="data row484 col0" >$1.91</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row484_col1" class="data row484 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row484_col2" class="data row484 col2" >$1.91</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row485" class="row_heading level0 row485" >Isri49</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row485_col0" class="data row485 col0" >$1.91</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row485_col1" class="data row485 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row485_col2" class="data row485 col2" >$1.91</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row486" class="row_heading level0 row486" >Ristydru66</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row486_col0" class="data row486 col0" >$1.91</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row486_col1" class="data row486 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row486_col2" class="data row486 col2" >$1.91</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row487" class="row_heading level0 row487" >Saralp86</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row487_col0" class="data row487 col0" >$1.88</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row487_col1" class="data row487 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row487_col2" class="data row487 col2" >$1.88</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row488" class="row_heading level0 row488" >Aerillorin70</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row488_col0" class="data row488 col0" >$1.88</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row488_col1" class="data row488 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row488_col2" class="data row488 col2" >$1.88</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row489" class="row_heading level0 row489" >Ailaesuir66</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row489_col0" class="data row489 col0" >$1.88</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row489_col1" class="data row489 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row489_col2" class="data row489 col2" >$1.88</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row490" class="row_heading level0 row490" >Yalaeria91</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row490_col0" class="data row490 col0" >$1.88</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row490_col1" class="data row490 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row490_col2" class="data row490 col2" >$1.88</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row491" class="row_heading level0 row491" >Ethralan59</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row491_col0" class="data row491 col0" >$1.85</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row491_col1" class="data row491 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row491_col2" class="data row491 col2" >$1.85</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row492" class="row_heading level0 row492" >Sundastnya66</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row492_col0" class="data row492 col0" >$1.85</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row492_col1" class="data row492 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row492_col2" class="data row492 col2" >$1.85</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row493" class="row_heading level0 row493" >Eoral49</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row493_col0" class="data row493 col0" >$1.84</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row493_col1" class="data row493 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row493_col2" class="data row493 col2" >$1.84</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row494" class="row_heading level0 row494" >Lirtyrdesta65</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row494_col0" class="data row494 col0" >$1.84</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row494_col1" class="data row494 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row494_col2" class="data row494 col2" >$1.84</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row495" class="row_heading level0 row495" >Phaedan76</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row495_col0" class="data row495 col0" >$1.84</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row495_col1" class="data row495 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row495_col2" class="data row495 col2" >$1.84</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row496" class="row_heading level0 row496" >Aillyriadru65</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row496_col0" class="data row496 col0" >$1.84</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row496_col1" class="data row496 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row496_col2" class="data row496 col2" >$1.84</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row497" class="row_heading level0 row497" >Sondassasya91</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row497_col0" class="data row497 col0" >$1.82</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row497_col1" class="data row497 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row497_col2" class="data row497 col2" >$1.82</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row498" class="row_heading level0 row498" >Aesty51</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row498_col0" class="data row498 col0" >$1.82</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row498_col1" class="data row498 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row498_col2" class="data row498 col2" >$1.82</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row499" class="row_heading level0 row499" >Chadadarya31</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row499_col0" class="data row499 col0" >$1.82</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row499_col1" class="data row499 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row499_col2" class="data row499 col2" >$1.82</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row500" class="row_heading level0 row500" >Ermol76</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row500_col0" class="data row500 col0" >$1.79</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row500_col1" class="data row500 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row500_col2" class="data row500 col2" >$1.79</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row501" class="row_heading level0 row501" >Iskassa50</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row501_col0" class="data row501 col0" >$1.79</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row501_col1" class="data row501 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row501_col2" class="data row501 col2" >$1.79</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row502" class="row_heading level0 row502" >Lirtossanya27</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row502_col0" class="data row502 col0" >$1.79</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row502_col1" class="data row502 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row502_col2" class="data row502 col2" >$1.79</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row503" class="row_heading level0 row503" >Saidairiaphos61</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row503_col0" class="data row503 col0" >$1.77</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row503_col1" class="data row503 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row503_col2" class="data row503 col2" >$1.77</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row504" class="row_heading level0 row504" >Silideu44</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row504_col0" class="data row504 col0" >$1.77</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row504_col1" class="data row504 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row504_col2" class="data row504 col2" >$1.77</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row505" class="row_heading level0 row505" >Assesi91</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row505_col0" class="data row505 col0" >$1.73</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row505_col1" class="data row505 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row505_col2" class="data row505 col2" >$1.73</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row506" class="row_heading level0 row506" >Aidaira48</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row506_col0" class="data row506 col0" >$1.73</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row506_col1" class="data row506 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row506_col2" class="data row506 col2" >$1.73</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row507" class="row_heading level0 row507" >Tanimnya91</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row507_col0" class="data row507 col0" >$1.73</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row507_col1" class="data row507 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row507_col2" class="data row507 col2" >$1.73</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row508" class="row_heading level0 row508" >Heosurnuru52</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row508_col0" class="data row508 col0" >$1.73</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row508_col1" class="data row508 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row508_col2" class="data row508 col2" >$1.73</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row509" class="row_heading level0 row509" >Phalinun47</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row509_col0" class="data row509 col0" >$1.73</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row509_col1" class="data row509 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row509_col2" class="data row509 col2" >$1.73</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row510" class="row_heading level0 row510" >Quelaton80</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row510_col0" class="data row510 col0" >$1.72</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row510_col1" class="data row510 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row510_col2" class="data row510 col2" >$1.72</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row511" class="row_heading level0 row511" >Silaera56</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row511_col0" class="data row511 col0" >$1.72</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row511_col1" class="data row511 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row511_col2" class="data row511 col2" >$1.72</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row512" class="row_heading level0 row512" >Aidaira26</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row512_col0" class="data row512 col0" >$1.72</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row512_col1" class="data row512 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row512_col2" class="data row512 col2" >$1.72</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row513" class="row_heading level0 row513" >Hala31</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row513_col0" class="data row513 col0" >$1.72</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row513_col1" class="data row513 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row513_col2" class="data row513 col2" >$1.72</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row514" class="row_heading level0 row514" >Aerithnuphos61</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row514_col0" class="data row514 col0" >$1.69</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row514_col1" class="data row514 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row514_col2" class="data row514 col2" >$1.69</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row515" class="row_heading level0 row515" >Tyiaduenuru55</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row515_col0" class="data row515 col0" >$1.69</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row515_col1" class="data row515 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row515_col2" class="data row515 col2" >$1.69</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row516" class="row_heading level0 row516" >Philistirap41</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row516_col0" class="data row516 col0" >$1.69</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row516_col1" class="data row516 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row516_col2" class="data row516 col2" >$1.69</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row517" class="row_heading level0 row517" >Aenarap34</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row517_col0" class="data row517 col0" >$1.65</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row517_col1" class="data row517 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row517_col2" class="data row517 col2" >$1.65</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row518" class="row_heading level0 row518" >Lisirrast82</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row518_col0" class="data row518 col0" >$1.59</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row518_col1" class="data row518 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row518_col2" class="data row518 col2" >$1.59</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row519" class="row_heading level0 row519" >Lisico81</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row519_col0" class="data row519 col0" >$1.59</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row519_col1" class="data row519 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row519_col2" class="data row519 col2" >$1.59</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row520" class="row_heading level0 row520" >Hallysucal81</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row520_col0" class="data row520 col0" >$1.59</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row520_col1" class="data row520 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row520_col2" class="data row520 col2" >$1.59</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row521" class="row_heading level0 row521" >Salilis27</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row521_col0" class="data row521 col0" >$1.56</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row521_col1" class="data row521 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row521_col2" class="data row521 col2" >$1.56</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row522" class="row_heading level0 row522" >Lisassa39</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row522_col0" class="data row522 col0" >$1.56</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row522_col1" class="data row522 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row522_col2" class="data row522 col2" >$1.56</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row523" class="row_heading level0 row523" >Aelollo59</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row523_col0" class="data row523 col0" >$1.55</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row523_col1" class="data row523 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row523_col2" class="data row523 col2" >$1.55</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row524" class="row_heading level0 row524" >Yararmol43</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row524_col0" class="data row524 col0" >$1.55</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row524_col1" class="data row524 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row524_col2" class="data row524 col2" >$1.55</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row525" class="row_heading level0 row525" >Tyeulisu40</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row525_col0" class="data row525 col0" >$1.55</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row525_col1" class="data row525 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row525_col2" class="data row525 col2" >$1.55</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row526" class="row_heading level0 row526" >Sally64</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row526_col0" class="data row526 col0" >$1.55</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row526_col1" class="data row526 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row526_col2" class="data row526 col2" >$1.55</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row527" class="row_heading level0 row527" >Lisosianya62</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row527_col0" class="data row527 col0" >$1.55</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row527_col1" class="data row527 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row527_col2" class="data row527 col2" >$1.55</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row528" class="row_heading level0 row528" >Lamyon68</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row528_col0" class="data row528 col0" >$1.55</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row528_col1" class="data row528 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row528_col2" class="data row528 col2" >$1.55</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row529" class="row_heading level0 row529" >Raeri71</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row529_col0" class="data row529 col0" >$1.50</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row529_col1" class="data row529 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row529_col2" class="data row529 col2" >$1.50</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row530" class="row_heading level0 row530" >Chanirra56</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row530_col0" class="data row530 col0" >$1.50</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row530_col1" class="data row530 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row530_col2" class="data row530 col2" >$1.50</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row531" class="row_heading level0 row531" >Lamil70</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row531_col0" class="data row531 col0" >$1.49</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row531_col1" class="data row531 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row531_col2" class="data row531 col2" >$1.49</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row532" class="row_heading level0 row532" >Eoduenurin62</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row532_col0" class="data row532 col0" >$1.49</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row532_col1" class="data row532 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row532_col2" class="data row532 col2" >$1.49</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row533" class="row_heading level0 row533" >Tyeuduen32</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row533_col0" class="data row533 col0" >$1.49</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row533_col1" class="data row533 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row533_col2" class="data row533 col2" >$1.49</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row534" class="row_heading level0 row534" >Philodil43</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row534_col0" class="data row534 col0" >$1.49</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row534_col1" class="data row534 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row534_col2" class="data row534 col2" >$1.49</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row535" class="row_heading level0 row535" >Sialaera37</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row535_col0" class="data row535 col0" >$1.49</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row535_col1" class="data row535 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row535_col2" class="data row535 col2" >$1.49</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row536" class="row_heading level0 row536" >Aisur51</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row536_col0" class="data row536 col0" >$1.49</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row536_col1" class="data row536 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row536_col2" class="data row536 col2" >$1.49</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row537" class="row_heading level0 row537" >Ilosia37</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row537_col0" class="data row537 col0" >$1.48</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row537_col1" class="data row537 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row537_col2" class="data row537 col2" >$1.48</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row538" class="row_heading level0 row538" >Pheodai94</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row538_col0" class="data row538 col0" >$1.48</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row538_col1" class="data row538 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row538_col2" class="data row538 col2" >$1.48</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row539" class="row_heading level0 row539" >Hiral75</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row539_col0" class="data row539 col0" >$1.45</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row539_col1" class="data row539 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row539_col2" class="data row539 col2" >$1.45</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row540" class="row_heading level0 row540" >Chanassa48</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row540_col0" class="data row540 col0" >$1.39</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row540_col1" class="data row540 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row540_col2" class="data row540 col2" >$1.39</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row541" class="row_heading level0 row541" >Chrathybust28</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row541_col0" class="data row541 col0" >$1.36</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row541_col1" class="data row541 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row541_col2" class="data row541 col2" >$1.36</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row542" class="row_heading level0 row542" >Chanastnya43</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row542_col0" class="data row542 col0" >$1.36</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row542_col1" class="data row542 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row542_col2" class="data row542 col2" >$1.36</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row543" class="row_heading level0 row543" >Rithe53</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row543_col0" class="data row543 col0" >$1.36</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row543_col1" class="data row543 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row543_col2" class="data row543 col2" >$1.36</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row544" class="row_heading level0 row544" >Pheusrical25</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row544_col0" class="data row544 col0" >$1.36</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row544_col1" class="data row544 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row544_col2" class="data row544 col2" >$1.36</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row545" class="row_heading level0 row545" >Isketo41</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row545_col0" class="data row545 col0" >$1.32</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row545_col1" class="data row545 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row545_col2" class="data row545 col2" >$1.32</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row546" class="row_heading level0 row546" >Tyaili86</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row546_col0" class="data row546 col0" >$1.28</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row546_col1" class="data row546 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row546_col2" class="data row546 col2" >$1.28</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row547" class="row_heading level0 row547" >Eollym91</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row547_col0" class="data row547 col0" >$1.28</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row547_col1" class="data row547 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row547_col2" class="data row547 col2" >$1.28</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row548" class="row_heading level0 row548" >Chamirra53</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row548_col0" class="data row548 col0" >$1.28</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row548_col1" class="data row548 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row548_col2" class="data row548 col2" >$1.28</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row549" class="row_heading level0 row549" >Ilaststa70</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row549_col0" class="data row549 col0" >$1.27</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row549_col1" class="data row549 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row549_col2" class="data row549 col2" >$1.27</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row550" class="row_heading level0 row550" >Aela59</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row550_col0" class="data row550 col0" >$1.27</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row550_col1" class="data row550 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row550_col2" class="data row550 col2" >$1.27</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row551" class="row_heading level0 row551" >Lassilsa63</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row551_col0" class="data row551 col0" >$1.27</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row551_col1" class="data row551 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row551_col2" class="data row551 col2" >$1.27</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row552" class="row_heading level0 row552" >Mindosiasya28</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row552_col0" class="data row552 col0" >$1.24</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row552_col1" class="data row552 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row552_col2" class="data row552 col2" >$1.24</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row553" class="row_heading level0 row553" >Raeduerin33</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row553_col0" class="data row553 col0" >$1.24</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row553_col1" class="data row553 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row553_col2" class="data row553 col2" >$1.24</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row554" class="row_heading level0 row554" >Heolo60</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row554_col0" class="data row554 col0" >$1.24</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row554_col1" class="data row554 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row554_col2" class="data row554 col2" >$1.24</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row555" class="row_heading level0 row555" >Ialidru40</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row555_col0" class="data row555 col0" >$1.24</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row555_col1" class="data row555 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row555_col2" class="data row555 col2" >$1.24</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row556" class="row_heading level0 row556" >Yaristi64</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row556_col0" class="data row556 col0" >$1.24</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row556_col1" class="data row556 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row556_col2" class="data row556 col2" >$1.24</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row557" class="row_heading level0 row557" >Ilrian97</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row557_col0" class="data row557 col0" >$1.24</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row557_col1" class="data row557 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row557_col2" class="data row557 col2" >$1.24</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row558" class="row_heading level0 row558" >Ryastycal90</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row558_col0" class="data row558 col0" >$1.21</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row558_col1" class="data row558 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row558_col2" class="data row558 col2" >$1.21</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row559" class="row_heading level0 row559" >Ilast79</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row559_col0" class="data row559 col0" >$1.20</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row559_col1" class="data row559 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row559_col2" class="data row559 col2" >$1.20</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row560" class="row_heading level0 row560" >Siasri67</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row560_col0" class="data row560 col0" >$1.20</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row560_col1" class="data row560 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row560_col2" class="data row560 col2" >$1.20</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row561" class="row_heading level0 row561" >Undirrasta74</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row561_col0" class="data row561 col0" >$1.16</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row561_col1" class="data row561 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row561_col2" class="data row561 col2" >$1.16</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row562" class="row_heading level0 row562" >Sundista85</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row562_col0" class="data row562 col0" >$1.14</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row562_col1" class="data row562 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row562_col2" class="data row562 col2" >$1.14</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row563" class="row_heading level0 row563" >Chamirrasya33</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row563_col0" class="data row563 col0" >$1.11</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row563_col1" class="data row563 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row563_col2" class="data row563 col2" >$1.11</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row564" class="row_heading level0 row564" >Eyircil84</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row564_col0" class="data row564 col0" >$1.06</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row564_col1" class="data row564 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row564_col2" class="data row564 col2" >$1.06</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row565" class="row_heading level0 row565" >Sondassa68</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row565_col0" class="data row565 col0" >$1.06</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row565_col1" class="data row565 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row565_col2" class="data row565 col2" >$1.06</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row566" class="row_heading level0 row566" >Lassadarsda57</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row566_col0" class="data row566 col0" >$1.03</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row566_col1" class="data row566 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row566_col2" class="data row566 col2" >$1.03</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row567" class="row_heading level0 row567" >Tridaira71</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row567_col0" class="data row567 col0" >$1.03</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row567_col1" class="data row567 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row567_col2" class="data row567 col2" >$1.03</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row568" class="row_heading level0 row568" >Rarith48</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row568_col0" class="data row568 col0" >$1.03</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row568_col1" class="data row568 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row568_col2" class="data row568 col2" >$1.03</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row569" class="row_heading level0 row569" >Alaesu91</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row569_col0" class="data row569 col0" >$1.03</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row569_col1" class="data row569 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row569_col2" class="data row569 col2" >$1.03</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row570" class="row_heading level0 row570" >Mindossa76</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row570_col0" class="data row570 col0" >$1.03</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row570_col1" class="data row570 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row570_col2" class="data row570 col2" >$1.03</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row571" class="row_heading level0 row571" >Lassista97</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row571_col0" class="data row571 col0" >$1.03</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row571_col1" class="data row571 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row571_col2" class="data row571 col2" >$1.03</td> 
    </tr>    <tr> 
        <th id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09level0_row572" class="row_heading level0 row572" >Ililsan66</th> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row572_col0" class="data row572 col0" >$1.03</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row572_col1" class="data row572 col1" >1</td> 
        <td id="T_1575b294_1c0b_11e8_9f0a_b0359fca2b09row572_col2" class="data row572 col2" >$1.03</td> 
    </tr></tbody> 
</table> 



# Most Popular Items


```python
# Identify the 5 most popular items by purchase count, then list (in a table):
# Item ID
# Item Name
# Purchase Count
# Item Price
# Total Purchase Value

```


```python
# gets a count of each item by grouping by Item ID and counting the number of each IDs occurances
top5_items_ID = pd.DataFrame(data_file_df.groupby('Item ID')['Item ID'].count())
top5_items_ID.head(10)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>3</td>
    </tr>
    <tr>
      <th>6</th>
      <td>3</td>
    </tr>
    <tr>
      <th>7</th>
      <td>6</td>
    </tr>
    <tr>
      <th>8</th>
      <td>6</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
#sort from high to low total purchase count
top5_items_ID.sort_values('Item ID', ascending = False, inplace = True)
top5_items_ID.head(10)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <td>11</td>
    </tr>
    <tr>
      <th>84</th>
      <td>11</td>
    </tr>
    <tr>
      <th>31</th>
      <td>9</td>
    </tr>
    <tr>
      <th>175</th>
      <td>9</td>
    </tr>
    <tr>
      <th>13</th>
      <td>9</td>
    </tr>
    <tr>
      <th>34</th>
      <td>9</td>
    </tr>
    <tr>
      <th>107</th>
      <td>8</td>
    </tr>
    <tr>
      <th>92</th>
      <td>8</td>
    </tr>
    <tr>
      <th>106</th>
      <td>8</td>
    </tr>
    <tr>
      <th>44</th>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
#keep the first 6 rows because there is a tie
top5_items_ID = top5_items_ID.iloc[0:6][:]
top5_items_ID
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <td>11</td>
    </tr>
    <tr>
      <th>84</th>
      <td>11</td>
    </tr>
    <tr>
      <th>31</th>
      <td>9</td>
    </tr>
    <tr>
      <th>175</th>
      <td>9</td>
    </tr>
    <tr>
      <th>13</th>
      <td>9</td>
    </tr>
    <tr>
      <th>34</th>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
#find the total purchase value of each item
top5_items_total = pd.DataFrame(data_file_df.groupby('Item ID')['Price'].sum())
top5_items_total.head(10)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.82</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9.12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.40</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.79</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2.28</td>
    </tr>
    <tr>
      <th>5</th>
      <td>3.96</td>
    </tr>
    <tr>
      <th>6</th>
      <td>3.60</td>
    </tr>
    <tr>
      <th>7</th>
      <td>27.06</td>
    </tr>
    <tr>
      <th>8</th>
      <td>23.46</td>
    </tr>
    <tr>
      <th>9</th>
      <td>4.08</td>
    </tr>
  </tbody>
</table>
</div>




```python
#merge purcahse count and total purcahse value 
top5_items = pd.merge(top5_items_ID, top5_items_total, left_index = True, right_index = True)
top5_items.head(10)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Price</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <td>11</td>
      <td>25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <td>11</td>
      <td>24.53</td>
    </tr>
    <tr>
      <th>31</th>
      <td>9</td>
      <td>18.63</td>
    </tr>
    <tr>
      <th>175</th>
      <td>9</td>
      <td>11.16</td>
    </tr>
    <tr>
      <th>13</th>
      <td>9</td>
      <td>13.41</td>
    </tr>
    <tr>
      <th>34</th>
      <td>9</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>107</th>
      <td>8</td>
      <td>28.88</td>
    </tr>
    <tr>
      <th>92</th>
      <td>8</td>
      <td>10.88</td>
    </tr>
    <tr>
      <th>106</th>
      <td>8</td>
      <td>18.32</td>
    </tr>
    <tr>
      <th>44</th>
      <td>8</td>
      <td>19.68</td>
    </tr>
  </tbody>
</table>
</div>




```python
#drop duplicate items from original Df
no_dup_items = data_file_df.drop_duplicates(['Item ID'], keep = 'last')
no_dup_items.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>17</th>
      <td>22</td>
      <td>Female</td>
      <td>59</td>
      <td>Lightning, Etcher of the King</td>
      <td>1.65</td>
      <td>Aenarap34</td>
    </tr>
    <tr>
      <th>21</th>
      <td>15</td>
      <td>Male</td>
      <td>3</td>
      <td>Phantomlight</td>
      <td>1.79</td>
      <td>Iaralrgue74</td>
    </tr>
    <tr>
      <th>59</th>
      <td>15</td>
      <td>Male</td>
      <td>2</td>
      <td>Verdict</td>
      <td>3.40</td>
      <td>Ila44</td>
    </tr>
    <tr>
      <th>63</th>
      <td>23</td>
      <td>Male</td>
      <td>28</td>
      <td>Flux, Destroyer of Due Diligence</td>
      <td>3.04</td>
      <td>Ryanara76</td>
    </tr>
    <tr>
      <th>88</th>
      <td>23</td>
      <td>Male</td>
      <td>132</td>
      <td>Persuasion</td>
      <td>3.90</td>
      <td>Undotesta33</td>
    </tr>
  </tbody>
</table>
</div>




```python
# merge to get all other info from the top 6 using the no dup df
top5_merge_ID = pd.merge(top5_items, no_dup_items, left_index = True, right_on = 'Item ID')
top5_merge_ID.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Item ID_x</th>
      <th>Price_x</th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID_y</th>
      <th>Item Name</th>
      <th>Price_y</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>721</th>
      <td>39</td>
      <td>11</td>
      <td>25.85</td>
      <td>26</td>
      <td>Male</td>
      <td>39</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>2.35</td>
      <td>Aeduera68</td>
    </tr>
    <tr>
      <th>766</th>
      <td>84</td>
      <td>11</td>
      <td>24.53</td>
      <td>22</td>
      <td>Female</td>
      <td>84</td>
      <td>Arcane Gem</td>
      <td>2.23</td>
      <td>Nitherian58</td>
    </tr>
    <tr>
      <th>772</th>
      <td>31</td>
      <td>9</td>
      <td>18.63</td>
      <td>15</td>
      <td>Male</td>
      <td>31</td>
      <td>Trickster</td>
      <td>2.07</td>
      <td>Sidap51</td>
    </tr>
    <tr>
      <th>761</th>
      <td>175</td>
      <td>9</td>
      <td>11.16</td>
      <td>28</td>
      <td>Male</td>
      <td>175</td>
      <td>Woeful Adamantite Claymore</td>
      <td>1.24</td>
      <td>Raeduerin33</td>
    </tr>
    <tr>
      <th>765</th>
      <td>13</td>
      <td>9</td>
      <td>13.41</td>
      <td>15</td>
      <td>Male</td>
      <td>13</td>
      <td>Serenity</td>
      <td>1.49</td>
      <td>Aerithnucal56</td>
    </tr>
  </tbody>
</table>
</div>




```python
#keep only needed columns
top5_merge_ID = top5_merge_ID[['Item ID', 'Item Name', 'Item ID_x', 'Price_y', 'Price_x']]
top5_merge_ID.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Item ID_x</th>
      <th>Price_y</th>
      <th>Price_x</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>721</th>
      <td>39</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>11</td>
      <td>2.35</td>
      <td>25.85</td>
    </tr>
    <tr>
      <th>766</th>
      <td>84</td>
      <td>Arcane Gem</td>
      <td>11</td>
      <td>2.23</td>
      <td>24.53</td>
    </tr>
    <tr>
      <th>772</th>
      <td>31</td>
      <td>Trickster</td>
      <td>9</td>
      <td>2.07</td>
      <td>18.63</td>
    </tr>
    <tr>
      <th>761</th>
      <td>175</td>
      <td>Woeful Adamantite Claymore</td>
      <td>9</td>
      <td>1.24</td>
      <td>11.16</td>
    </tr>
    <tr>
      <th>765</th>
      <td>13</td>
      <td>Serenity</td>
      <td>9</td>
      <td>1.49</td>
      <td>13.41</td>
    </tr>
  </tbody>
</table>
</div>




```python
#resetting index as item ID for aesthetics
top5_merge_ID.set_index(['Item ID'], inplace = True)
top5_merge_ID.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item Name</th>
      <th>Item ID_x</th>
      <th>Price_y</th>
      <th>Price_x</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>11</td>
      <td>2.35</td>
      <td>25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <td>Arcane Gem</td>
      <td>11</td>
      <td>2.23</td>
      <td>24.53</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Trickster</td>
      <td>9</td>
      <td>2.07</td>
      <td>18.63</td>
    </tr>
    <tr>
      <th>175</th>
      <td>Woeful Adamantite Claymore</td>
      <td>9</td>
      <td>1.24</td>
      <td>11.16</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Serenity</td>
      <td>9</td>
      <td>1.49</td>
      <td>13.41</td>
    </tr>
  </tbody>
</table>
</div>




```python
# renaming the columns
top5_merge_ID.rename(columns =  {'Item ID_x': 'Purchase Count', 'Price_y': 'Item Price', 
                                 'Price_x': 'Total Purchase Value'}, inplace=True)
top5_merge_ID.head(10)
```

    C:\Users\lawre\Anaconda3\lib\site-packages\pandas\core\frame.py:2746: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      **kwargs)
    




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item Name</th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>11</td>
      <td>2.35</td>
      <td>25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <td>Arcane Gem</td>
      <td>11</td>
      <td>2.23</td>
      <td>24.53</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Trickster</td>
      <td>9</td>
      <td>2.07</td>
      <td>18.63</td>
    </tr>
    <tr>
      <th>175</th>
      <td>Woeful Adamantite Claymore</td>
      <td>9</td>
      <td>1.24</td>
      <td>11.16</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Serenity</td>
      <td>9</td>
      <td>1.49</td>
      <td>13.41</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Retribution Axe</td>
      <td>9</td>
      <td>4.14</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>107</th>
      <td>Splitter, Foe Of Subtlety</td>
      <td>8</td>
      <td>3.61</td>
      <td>28.88</td>
    </tr>
    <tr>
      <th>92</th>
      <td>Final Critic</td>
      <td>8</td>
      <td>1.36</td>
      <td>10.88</td>
    </tr>
    <tr>
      <th>106</th>
      <td>Crying Steel Sickle</td>
      <td>8</td>
      <td>2.29</td>
      <td>18.32</td>
    </tr>
    <tr>
      <th>44</th>
      <td>Bonecarvin Battle Axe</td>
      <td>8</td>
      <td>2.46</td>
      <td>19.68</td>
    </tr>
  </tbody>
</table>
</div>




```python
#formating the DataFrame
top5_merge_ID.style.format({'Item Price': '${:.2f}', 'Total Purchase Value': '${:.2f}'})
top5_merge_ID.head(10)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item Name</th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>11</td>
      <td>2.35</td>
      <td>25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <td>Arcane Gem</td>
      <td>11</td>
      <td>2.23</td>
      <td>24.53</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Trickster</td>
      <td>9</td>
      <td>2.07</td>
      <td>18.63</td>
    </tr>
    <tr>
      <th>175</th>
      <td>Woeful Adamantite Claymore</td>
      <td>9</td>
      <td>1.24</td>
      <td>11.16</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Serenity</td>
      <td>9</td>
      <td>1.49</td>
      <td>13.41</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Retribution Axe</td>
      <td>9</td>
      <td>4.14</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>107</th>
      <td>Splitter, Foe Of Subtlety</td>
      <td>8</td>
      <td>3.61</td>
      <td>28.88</td>
    </tr>
    <tr>
      <th>92</th>
      <td>Final Critic</td>
      <td>8</td>
      <td>1.36</td>
      <td>10.88</td>
    </tr>
    <tr>
      <th>106</th>
      <td>Crying Steel Sickle</td>
      <td>8</td>
      <td>2.29</td>
      <td>18.32</td>
    </tr>
    <tr>
      <th>44</th>
      <td>Bonecarvin Battle Axe</td>
      <td>8</td>
      <td>2.46</td>
      <td>19.68</td>
    </tr>
  </tbody>
</table>
</div>



# Most Profitable Items


```python

# Identify the 5 most profitable items by total purchase value, then list (in a table):
# Item ID
# Item Name
# Purchase Count
# Item Price
# Total Purchase Value
```


```python
# find total purcahse value and sort by high to low
top5_profit = pd.DataFrame(data_file_df.groupby('Item ID')['Price'].sum())
top5_profit.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.82</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9.12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.40</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.79</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2.28</td>
    </tr>
  </tbody>
</table>
</div>




```python
top5_profit.sort_values('Price', ascending = False, inplace = True)
top5_profit.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <td>37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <td>29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <td>29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <td>29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>




```python
#get item purchase count
pur_count_profit = pd.DataFrame(data_file_df.groupby('Item ID')['Item ID'].count())
pur_count_profit.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
top5_profit = pd.merge(top5_profit, pur_count_profit, left_index = True, right_index = True, how = 'left')
top5_profit.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Price</th>
      <th>Item ID_x</th>
      <th>Item ID_y</th>
      <th>Item ID</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <td>37.26</td>
      <td>9</td>
      <td>9</td>
      <td>9</td>
    </tr>
    <tr>
      <th>115</th>
      <td>29.75</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
    </tr>
    <tr>
      <th>32</th>
      <td>29.70</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <th>103</th>
      <td>29.22</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <th>107</th>
      <td>28.88</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
top5_merge_profit = pd.merge(top5_profit, no_dup_items, left_index = True, right_on = 'Item ID', how = 'left')
top5_merge_profit.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Price_x</th>
      <th>Item ID_x</th>
      <th>Item ID_y</th>
      <th>Item ID_x</th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID_y</th>
      <th>Item Name</th>
      <th>Price_y</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>746</th>
      <td>34</td>
      <td>37.26</td>
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>35</td>
      <td>Male</td>
      <td>34</td>
      <td>Retribution Axe</td>
      <td>4.14</td>
      <td>Ralasti48</td>
    </tr>
    <tr>
      <th>705</th>
      <td>115</td>
      <td>29.75</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>25</td>
      <td>Male</td>
      <td>115</td>
      <td>Spectral Diamond Doomblade</td>
      <td>4.25</td>
      <td>Aeral85</td>
    </tr>
    <tr>
      <th>657</th>
      <td>32</td>
      <td>29.70</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>28</td>
      <td>Male</td>
      <td>32</td>
      <td>Orenmir</td>
      <td>4.95</td>
      <td>Tyarithn67</td>
    </tr>
    <tr>
      <th>716</th>
      <td>103</td>
      <td>29.22</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>9</td>
      <td>Male</td>
      <td>103</td>
      <td>Singed Scalpel</td>
      <td>4.87</td>
      <td>Ilophos58</td>
    </tr>
    <tr>
      <th>779</th>
      <td>107</td>
      <td>28.88</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>23</td>
      <td>Female</td>
      <td>107</td>
      <td>Splitter, Foe Of Subtlety</td>
      <td>3.61</td>
      <td>Alim85</td>
    </tr>
  </tbody>
</table>
</div>




```python
top5_merge_profit = top5_merge_profit[['Item ID', 'Item Name', 'Item ID_x', 'Price_y','Price_x']]
top5_merge_profit.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Item ID_x</th>
      <th>Item ID_x</th>
      <th>Price_y</th>
      <th>Price_x</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>746</th>
      <td>34</td>
      <td>Retribution Axe</td>
      <td>9</td>
      <td>9</td>
      <td>4.14</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>705</th>
      <td>115</td>
      <td>Spectral Diamond Doomblade</td>
      <td>7</td>
      <td>7</td>
      <td>4.25</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>657</th>
      <td>32</td>
      <td>Orenmir</td>
      <td>6</td>
      <td>6</td>
      <td>4.95</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>716</th>
      <td>103</td>
      <td>Singed Scalpel</td>
      <td>6</td>
      <td>6</td>
      <td>4.87</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>779</th>
      <td>107</td>
      <td>Splitter, Foe Of Subtlety</td>
      <td>8</td>
      <td>8</td>
      <td>3.61</td>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>




```python
top5_merge_profit.set_index(['Item ID'], inplace=True)
top5_merge_profit.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item Name</th>
      <th>Item ID_x</th>
      <th>Item ID_x</th>
      <th>Price_y</th>
      <th>Price_x</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <td>Retribution Axe</td>
      <td>9</td>
      <td>9</td>
      <td>4.14</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <td>Spectral Diamond Doomblade</td>
      <td>7</td>
      <td>7</td>
      <td>4.25</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Orenmir</td>
      <td>6</td>
      <td>6</td>
      <td>4.95</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <td>Singed Scalpel</td>
      <td>6</td>
      <td>6</td>
      <td>4.87</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <td>Splitter, Foe Of Subtlety</td>
      <td>8</td>
      <td>8</td>
      <td>3.61</td>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>




```python
top5_merge_profit.rename(columns = {'Item ID_x': 'Purchase Count', 'Price_y': 'Item Price', 
                                    'Price_x': 'Total Purchase Value'}, inplace = True)
top5_merge_profit.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item Name</th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <td>Retribution Axe</td>
      <td>9</td>
      <td>4.14</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <td>Spectral Diamond Doomblade</td>
      <td>7</td>
      <td>4.25</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Orenmir</td>
      <td>6</td>
      <td>4.95</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <td>Singed Scalpel</td>
      <td>6</td>
      <td>4.87</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <td>Splitter, Foe Of Subtlety</td>
      <td>8</td>
      <td>3.61</td>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>




```python
top5_merge_profit.style.format({'Item Price': '${:.2f}', 'Total Purchase Value': '${:.2f}'})
top5_merge_profit.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item Name</th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <td>Retribution Axe</td>
      <td>9</td>
      <td>4.14</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <td>Spectral Diamond Doomblade</td>
      <td>7</td>
      <td>4.25</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Orenmir</td>
      <td>6</td>
      <td>4.95</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <td>Singed Scalpel</td>
      <td>6</td>
      <td>4.87</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <td>Splitter, Foe Of Subtlety</td>
      <td>8</td>
      <td>3.61</td>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>




```python
# My Observation
1. The percentage of Male Participant is greatly more than the Female Participant
2. The age bin Frame of 10-14, the Average purchase price is Lower than than the Age-bin 40 
3. Another thing that i observed was merging the dataFrame together there values in some columns and rows that are duplicating, and that was why there is a need to do some cleanups like renaming columns etc.
```
