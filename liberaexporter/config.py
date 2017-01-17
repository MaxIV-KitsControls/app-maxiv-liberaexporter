""" 
List all gauges metrics here with order (Name, Description, libera-node-path, labels (optional))
Information was taken from Libera Brilliance Plus user manual (5.4.5.2. Sensor read-out and description)
"""

gauges_temp_raf_list = [
                    ("temp_MAX6698_LOCAL", "Internal chip temperature. This chip controls sensors", "boards.raf{0}.sensors.ID_1.value"),
                    ("temp_FPGA", "Temperature inside FPGA chip", "boards.raf{0}.sensors.ID_2.value"),
                    ("temp_ADC_1", "Temperature around the ADC area", "boards.raf{0}.sensors.ID_3.value"),
                    ("temp_ADC_2", "Temperature around ADC clock distributor", "boards.raf{0}.sensors.ID_4.value"),
                    ("temp_AIRFLOW", "Temperature of the airflow passing through the board", "boards.raf{0}.sensors.ID_5.value"),
                    ("temp_1", "Temperature around RF chains 'C & D' ", "boards.raf{0}.sensors.ID_6.value"),
                    ("temp_2", "Temperature around RF chains 'A & B' ", "boards.raf{0}.sensors.ID_7.value"),
                ]


gauges_temp_evrx_list = [
                    ("evrx_temp_MAX6698_LOCAL", "Internal chip temperature. This chip controls sensors", "boards.evrx2.sensors.ID_1.value"),
                    ("evrx_temp_POWR_SUPP_1", "Temperature around highly loaded power supply.", "boards.evrx2.sensors.ID_2.value"),
                    ("evrx_temp_FPGA", "Temperature inside FPGA chip", "boards.evrx2.sensors.ID_3.value"),
                    ("raf_temp_NC", "Not connected", "boards.evrx2.sensors.ID_4.value"),
                    ("evrx_temp_INPUTS", "Temperature around input buffers.", "boards.evrx2.sensors.ID_5.value"),
                    ("evrx_temp_POWR_SUPP_2", "Temperature around highly loaded power supply.", "boards.evrx2.sensors.ID_6.value"),
                    ("evrx_temp_AIRFLOW", "Temperature of the airflow passing through the board.", "boards.evrx2.sensors.ID_7.value"),
                ]


# gauges_temp_icb_list = [
#                     ("evrx_temp_MAX6698_LOCAL", "Internal chip temperature. This chip controls sensors", "boards.evrx2.sensors.ID_1.value"),
#                     ("evrx_temp_POWR_SUPP_1", "Temperature around highly loaded power supply.", "boards.evrx2.sensors.ID_2.value"),
#                     ("evrx_temp_FPGA", "Temperature inside FPGA chip", "boards.evrx2.sensors.ID_3.value"),
#                     ("raf_temp_NC", "Not connected", "boards.evrx2.sensors.ID_4.value"),
#                     ("evrx_temp_INPUTS", "Temperature around input buffers.", "boards.evrx2.sensors.ID_5.value"),
#                     ("evrx_temp_POWR_SUPP_2", "Temperature around highly loaded power supply.", "boards.evrx2.sensors.ID_6.value"),
#                     ("evrx_temp_AIRFLOW", "Temperature of the airflow passing through the board.", "boards.evrx2.sensors.ID_7.value"),
#                 ]
