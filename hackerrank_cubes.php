<?php

class Cube {
    
    /**
     * Size of the cube.
     * @var int
     */
    protected $size;
    
    /**
     * Data for the cube.
     * @var array
     */
    protected $data = array ();
    
    /**
     * Creates a Cube object with specified size.
     * @param int $size Size of the cube.
     */
    public function __construct($size) {
        $this->size = $size;
    }
    
    /**
     * Sets the value at x, y, z position of the cube.
     * @param int $x
     * @param int $y
     * @param int $z
     * @param int $value
     * @return mixed False on failure
     */
    public function update($x, $y, $z, $value) {
        $index = $x . ':' . $y . ':' . $z;
        $this->data[$index] = array (
            'x' => $x,
            'y' => $y,
            'z' => $z,
            'value' => $value,
        );
    }
    
    /**
     * Returns the sum of values in the cube between x1, y1, z1 and x2, y2, z2.
     * Returns FALSE if the positions are invalid.
     * @param int $x1
     * @param int $y1
     * @param int $z1
     * @param int $x2
     * @param int $y2
     * @param int $z2
     * @return int|boolean Sum of values or FALSE if positions are invalid.
     */
    public function query($x1, $y1, $z1, $x2, $y2, $z2) {
        
        // Compute sum
        $output = 0;
        foreach ($this->data as $point):
            if ($point['x'] < $x1 || $point['x'] > $x2 )
                continue;
            if ($point['y'] < $y1 || $point['y'] > $y2 )
                continue;
            if ($point['z'] < $z1 || $point['z'] > $z2 )
                continue;
            $output += $point['value'];
        endforeach;
        return $output;
        
    }
    
}

// Input output
#$handle = fopen("php://stdin", "r");
$handle = fopen("cube_orders.txt", "r");
//$handle = fopen("cube-summation.input", "r");

$test_case_count = fgets($handle);
for ($test_case = 0; $test_case < $test_case_count; $test_case++):

    $line = fgets($handle);
    list ($size, $query_count) = sscanf($line, '%d %d');

    // Create cube
    $cube = new Cube($size);

    // Validate number of queries
    if ($query_count < 1 || $query_count > 1000)
        return FALSE;

    // Execute queries
    for ($query_i = 0; $query_i < $query_count; $query_i++):

        $query = fgets($handle);
        $query = trim($query);
        $query_parts = explode(' ', $query);

        if (5 === sizeof($query_parts)) {
            $cube->update($query_parts[1], $query_parts[2], $query_parts[3], $query_parts[4]);
        }
        else {
            echo $cube->query($query_parts[1], $query_parts[2], $query_parts[3], $query_parts[4], $query_parts[5], $query_parts[6]) . "\n";
        }

    endfor;

endfor;

fclose($handle);