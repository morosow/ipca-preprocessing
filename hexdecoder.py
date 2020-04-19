import pandas as pd
import codecs

input_filename = 'input.csv'
output_filename = 'output.csv'

df = pd.read_csv(input_filename, sep = ';', header=0, skip_blank_lines=True, error_bad_lines=False)

df.index = range(0, len(df.index))

# In this case values (to decoding) are contained in 'description' column

# Deleting '0x' from strings begin
df.description = df.description.apply(lambda x: x[2:])

# Converting hex to utf
df.description = df.description.apply(lambda x: codecs.decode(x, "hex").decode('utf-8'))

df.to_csv(output_filename, header=True, sep=';', index=False)
