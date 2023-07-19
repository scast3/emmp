
function power(q, h, n) {
    const density = 62.4;
    const g = 32.2;
    const power = (q * h * density * g) / (550 * n);
    console.log(power);
    return power;
}

function powerdif(flow1, head1, efficiency1, flow2, head2, efficiency2) {
    // Calculate power for Pump 1
    const power1 = power(flow1, head1, efficiency1);

    // Calculate power for Pump 2
    const power2 = power(flow2, head2, efficiency2);

    // Calculate the difference in power
    const powerDifference = power2 - power1;

    return powerDifference;
}

function costs(power1,power2){
    return 1;
}