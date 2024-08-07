CREATE TABLE transacciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    empleado_id INT NOT NULL,
    ingreso_deduccion_id INT NOT NULL,
    tipo_transaccion VARCHAR(10) NOT NULL,
    fecha DATE NOT NULL,
    monto DECIMAL(10, 2) NOT NULL,
    estado BOOLEAN NOT NULL,
    FOREIGN KEY (empleado_id) REFERENCES empleados(id),
    FOREIGN KEY (ingreso_deduccion_id) REFERENCES tipos_ingresos(id)
);



