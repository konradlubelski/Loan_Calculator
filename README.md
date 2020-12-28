# Loan_Calculator
Loan calculator with different parameters which is launching through CLI.

Loan calculator with different parameters which is launching through CLI.
Main assumptions:
- the --type and --interest parameters must always be specified
- types of arguments
	|  argument |  type  |
	|  :---: |  :---:  |
	|  --type |  string: "diff" or "annuity"  |
	|  --principal |  positive int  |
	|  --payment |  positive float  |
	|  --periods |  positive int  |
	|  --interest |  positive float  |
	
- calculation of differentiated payments. To do this, the user can run the program specifying interest, number of    monthly
	|  --type = diff  |  --principal  |  --payment  |  --periods  |  --interest  |
	|  :---: |  :---:  |  :---:  |  :---:  |  :---:  |
	|  x |  x  |  C  |  x  |  x  |
    
    example query:  “python loan_calculator_cmd.py --type=diff --principal=1000000 --periods=10 --interest=10”
- ability to calculate for annuity payment (principal, number of monthly payments, and monthly payment amount). The user specifies all the known parameters with command-line arguments, and one parameter will be unknown. This is the value the user wants to calculate.
  |  --type = annuity  |  --principal  |  --payment  |  --periods  |  --interest  |
  |  :---: |  :---:  |  :---:  |  :---:  |  :---:  |
  |  x |  x  |  C  |  x  |  x  |
  |  x |  C  |  x |  x  |  x  |
  |  x |  x  |  x  |  C  |  x  |
    
    example query:  “python loan_calculator_cmd.py --type=annuity --principal=1000000 --periods=10 --interest=10”


Educationnal goals:
- using CLI in projects
- learning about argparse and math libraries


	

	


