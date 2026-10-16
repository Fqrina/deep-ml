import numpy as np

def simple_conv2d(input_matrix: np.ndarray, kernel: np.ndarray, padding: int, stride: int):
	input_height, input_width = input_matrix.shape
	kernel_height, kernel_width = kernel.shape
	mat = np.zeros((input_height + 2*padding, input_width + 2*padding), dtype=np.float32)
	mat[padding:padding+input_height, padding:padding+input_width] = input_matrix
	retmatrix = []
	for j in range(0,len(mat)-kernel_height+1, stride):
		row = []
		for i in range(0, len(mat[0])-kernel_width+1, stride):
			convmat = mat[j:j+kernel_height, i:i+kernel_width]
			ans = np.sum(convmat * kernel)
			row.append(ans)
		retmatrix.append(row)
	return retmatrix
			
	print(input_matrix)

	# Your code here
    
	# return output_matrix
