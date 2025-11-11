import numpy as np
from sagittal_brain import run_averages

def test_sagittal_brain():
    data_input = np.random.randint(0, 10, (20, 20))

    np.savetxt("brain_sample.csv", data_input, fmt='%d', delimiter=',')

    expected = np.mean(data_input, axis=0)
    np.savetxt("expected.csv", expected, fmt='%d', delimiter=',')
    run_averages("brain_sample.csv", "brain_average.csv")

    output = np.loadtxt("brain_average.csv", delimiter=',')

    assert np.allclose(output, expected), "Output does not match expected result!"

if __name__ == "__main__":
    test_sagittal_brain()
