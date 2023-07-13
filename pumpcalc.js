function power(Q1,w1,h1,n1,Q2,w2,h2,n2){
    const density = 62.4; // Density of water in lb/ft³
    const g = 32.2; // Acceleration due to gravity in ft/s²
  
    // Calculate power for Pump 1
    const power1 = (flow1 * head1 * density * g) / (550 * efficiency1 * Math.pow(speed1, 3));
  
    // Calculate power for Pump 2
    const power2 = (flow2 * head2 * density * g) / (550 * efficiency2 * Math.pow(speed2, 3));
  
    // Calculate the difference in power
    const powerDifference = Math.abs(power1 - power2);
  
    return powerDifference;
}
function costs(){
    return 1;
}