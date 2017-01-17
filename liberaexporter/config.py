""" 
List all gauges metrics here with order (Name, Description, libera-node-path, labels (optional))
Information was taken from Libera Brilliance Plus user manual (5.4.5.2. Sensor read-out and description)
"""

gauges_raf_list = [ #RAF Board
                    #Temperatures
                    ("temp_MAX6698_LOCAL", "Internal chip temperature. This chip controls sensors", "boards.raf{0}.sensors.ID_1.value"),
                    ("temp_FPGA", "Temperature inside FPGA chip", "boards.raf{0}.sensors.ID_2.value"),
                    ("temp_ADC_1", "Temperature around the ADC area", "boards.raf{0}.sensors.ID_3.value"),
                    ("temp_ADC_2", "Temperature around ADC clock distributor", "boards.raf{0}.sensors.ID_4.value"),
                    ("temp_AIRFLOW", "Temperature of the airflow passing through the board", "boards.raf{0}.sensors.ID_5.value"),
                    ("temp_1", "Temperature around RF chains 'C & D' ", "boards.raf{0}.sensors.ID_6.value"),
                    ("temp_2", "Temperature around RF chains 'A & B' ", "boards.raf{0}.sensors.ID_7.value"),
                    #Voltage
                    ("volt_12V_AMC", "Voltage of 12V_AMC", "boards.raf{0}.sensors.ID_8.value"),
                    ("volt_7VRF", "Voltage of 7VRF", "boards.raf{0}.sensors.ID_9.value"),
                    ("volt_3V3", "Voltage of 3V3", "boards.raf{0}.sensors.ID_10.value"),
                    ("volt_2V5", "Voltage of 2V5", "boards.raf{0}.sensors.ID_11.value"),
                    ("volt_CFG3V", "Voltage of CFG3V", "boards.raf{0}.sensors.ID_12.value"),
                    ("volt_5VRF", "Voltage of 5VRF", "boards.raf{0}.sensors.ID_13.value"),
                    ("volt_1V8", "Voltage of  1V8", "boards.raf{0}.sensors.ID_14.value"),
                    ("volt_1V0_INT", "Voltage of 1V0_INT", "boards.raf{0}.sensors.ID_15.value"),
                    ("volt_1V2_GTP_PLL", "Voltage of 1V2_GTP_PLL", "boards.raf{0}.sensors.ID_16.value"),
                    ("volt_1V2_GTP", "Voltage of 1V2_GTP", "boards.raf{0}.sensors.ID_17.value"),
                    ("volt_1V_GTP", "Voltage of 1V_GTP", "boards.raf{0}.sensors.ID_18.value"),
                    ("volt_3V3MP", "Voltage of 3V3MP", "boards.raf{0}.sensors.ID_19.value"),
                ]


gauges_list = [
                #EVRX - Timing Board
                    #Temperatures
                    ("evrx_temp_MAX6698_LOCAL", "Internal chip temperature. This chip controls sensors", "boards.evrx2.sensors.ID_1.value"),
                    ("evrx_temp_POWR_SUPP_1", "Temperature around highly loaded power supply.", "boards.evrx2.sensors.ID_2.value"),
                    ("evrx_temp_FPGA", "Temperature inside FPGA chip", "boards.evrx2.sensors.ID_3.value"),
                    ("evrx_temp_NC", "Not connected", "boards.evrx2.sensors.ID_4.value"),
                    ("evrx_temp_INPUTS", "Temperature around input buffers.", "boards.evrx2.sensors.ID_5.value"),
                    ("evrx_temp_POWR_SUPP_2", "Temperature around highly loaded power supply.", "boards.evrx2.sensors.ID_6.value"),
                    ("evrx_temp_AIRFLOW", "Temperature of the airflow passing through the board.", "boards.evrx2.sensors.ID_7.value"),
                    #Voltage
                    ("evrx_volt_12V_AMC", "Voltage of 12V_AMC", "boards.evrx2.sensors.ID_8.value"),
                    ("evrx_volt_3V3MP", "Voltage of 3V3MP", "boards.evrx2.sensors.ID_9.value"),
                    ("evrx_volt_3V75", "Voltage of 3V75", "boards.evrx2.sensors.ID_12.value"),
                    ("evrx_volt_3V3", "Voltage of 3V3", "boards.evrx2.sensors.ID_13.value"),
                    ("evrx_volt_3V3CLK", "Voltage of 3V3CLK", "boards.evrx2.sensors.ID_14.value"),
                    ("evrx_volt_1V2", "Voltage of 1V2", "boards.evrx2.sensors.ID_15.value"),
                    ("evrx_volt_1V2MGT", "Voltage of 1V2MGT", "boards.evrx2.sensors.ID_16.value"),
                #ICB0 Board
                    #Temperatures
                    ("icb0_temp_MAX6698_LOCAL", "Internal chip temperature. This chip controls sensors", "boards.icb0.sensors.ID_0.value"),
                    ("icb0_temp_PLX", "Temperature around highly loaded power supply.", "boards.icb0.sensors.ID_1.value"),
                    ("icb0_temp_POWR_1", "Temperature around highly loaded power supplies.", "boards.icb0.sensors.ID_2.value"),
                    ("icb0_temp_POWR_2", "Temperature around highly loaded power supplies.", "boards.icb0.sensors.ID_3.value"),
                    ("evrx_temp_AIRFLOW_IN", "Temperature of the (board) in-take airflow", "boards.icb0.sensors.ID_4.value"),
                    ("evrx_temp_AIRFLOW_OUT", "Temperature of the (board) out-take airflow", "boards.icb0.sensors.ID_5.value"),
                    ("icb0_temp_BACKPLANE", "Temperature of the exhaust airflow from the instrument's power supply.", "boards.icb0.sensors.ID_6.value"), 
                    #Voltage
                    ("icb0_volt_1V2M", "Voltage of 1V2M", "boards.icb0.sensors.ID_7.value"),
                    ("icb0_volt_2V5PLX", "Voltage of 2V5PLX", "boards.icb0.sensors.ID_8.value"),
                    ("icb0_volt_1VPLX", "Voltage of 1VPLX", "boards.icb0.sensors.ID_9.value"),
                    ("icb0_volt_12V10", "Voltage of 12V10", "boards.icb0.sensors.ID_10.value"),
                    ("icb0_volt_5VM", "Voltage of 5VM", "boards.icb0.sensors.ID_11.value"),
                    ("icb0_volt_12VIN", "Voltage of 12VIN", "boards.icb0.sensors.ID_24.value"),
                    ("icb0_volt_3V3M", "Voltage of 3V3M", "boards.icb0.sensors.ID_25.value"),
                    ("icb0_volt_3V3IN", "Voltage of 3V3IN", "boards.icb0.sensors.ID_26.value"),
                    ("icb0_volt_2V5M", "Voltage of 2V5M", "boards.icb0.sensors.ID_27.value"),                    
                    #Current
                    ("icb0_curr_I3V3MON", "Current of I3V3MON", "boards.icb0.sensors.ID_12.value"),
                    ("icb0_curr_I12V1MON", "Current of I12V1MON", "boards.icb0.sensors.ID_13.value"),
                    ("icb0_curr_I12V2MON", "Current of I12V2MON", "boards.icb0.sensors.ID_14.value"),
                    ("icb0_curr_I12V3MON", "Current of I12V3MON", "boards.icb0.sensors.ID_15.value"),
                    ("icb0_curr_I12V4MON", "Current of I12V4MON", "boards.icb0.sensors.ID_16.value"),
                    ("icb0_curr_I12V5MON", "Current of I12V5MON", "boards.icb0.sensors.ID_17.value"),
                    ("icb0_curr_I12V6MON", "Current of I12V6MON", "boards.icb0.sensors.ID_18.value"),
                    ("icb0_curr_I12V7MON", "Current of I12V7MON", "boards.icb0.sensors.ID_19.value"),
                    ("icb0_curr_I12V8MON", "Current of I12V8MON", "boards.icb0.sensors.ID_20.value"),
                    ("icb0_curr_I12V9MON", "Current of I12V9MON", "boards.icb0.sensors.ID_21.value"),
                    ("icb0_curr_I12V10MON", "Current of I12V10MON", "boards.icb0.sensors.ID_22.value"),
                    ("icb0_curr_I12V11MON", "Current of I12V11MON", "boards.icb0.sensors.ID_23.value"),
                    #Fans
                    ("icb0_fan_LEFT_FAN1", "Fan Speed of LEFT.FAN1", "boards.icb0.sensors.ID_28.value"),                    
                    ("icb0_fan_LEFT_FAN2", "Fan Speed of LEFT.FAN2", "boards.icb0.sensors.ID_29.value"),                   
                    ("icb0_fan_LEFT_FAN3", "Fan Speed of LEFT.FAN3", "boards.icb0.sensors.ID_30.value"),                   
                    ("icb0_fan_RIGHT_FAN1", "Fan Speed of RIGHT.FAN1", "boards.icb0.sensors.ID_31.value"),                   
                    ("icb0_fan_RIGHT_FAN2", "Fan Speed of RIGHT.FAN2", "boards.icb0.sensors.ID_32.value"),                   
                    ("icb0_fan_RIGHT_FAN3", "Fan Speed of RIGHT.FAN3", "boards.icb0.sensors.ID_33.value"),                   
                #GDX Board
                    #Temperatures
                    ("gdx_temp_MAX6698_LOCAL", "Internal chip temperature. This chip controls sensors", "boards.gdx1.sensors.ID_1.value"),
                    ("gdx_temp_FPGA", "Temperature inside FPGA chip", "boards.gdx1.sensors.ID_2.value"),                    
                    ("gdx_temp_POWR_SUPP_1", "Temperature around highly loaded power supply.", "boards.gdx1.sensors.ID_3.value"),
                    ("gdx_temp_CENT_BOARD", "Temperature in central part of the board (no specific chip).", "boards.gdx1.sensors.ID_4.value"),
                    ("gdx_temp_MGT_SUPP", "Temperature of the SFP power supplies.", "boards.gdx1.sensors.ID_5.value"),
                    ("gdx_temp_AIRFLOW", "Temperature of the airflow passing through the board.", "boards.gdx1.sensors.ID_6.value"),                         
                    ("gdx_temp_DDR3_MODULE", "Temperature of the DDR3 memory (placed below the memory chip).", "boards.gdx1.sensors.ID_7.value"),
                    #Voltage
                    ("gdx_volt_12V_AMC", "Voltage of 12V_AMC", "boards.gdx1.sensors.ID_8.value"),
                    ("gdx_volt_3V3MP", "Voltage of 3V3MP", "boards.gdx1.sensors.ID_9.value"),
                    ("gdx_volt_3V3", "Voltage of 3V3", "boards.gdx1.sensors.ID_10.value"),
                    ("gdx_volt_2V5", "Voltage of 2V5", "boards.gdx1.sensors.ID_11.value"),
                    ("gdx_volt_2V5C", "Voltage of 2V5C", "boards.gdx1.sensors.ID_12.value"),
                    ("gdx_volt_1V2_GTX", "Voltage of 1V2_GTX", "boards.gdx1.sensors.ID_13.value"),
                    ("gdx_volt_1V0_INT", "Voltage of 1V0_INT", "boards.gdx1.sensors.ID_14.value"),
                    ("gdx_volt_1V0_GTX", "Voltage of 1V0_GTX", "boards.gdx1.sensors.ID_15.value"),
                    ("gdx_volt_0V75_VTT", "Voltage of 0V75_VTT", "boards.gdx1.sensors.ID_16.value"),
                    ("gdx_volt_1V5", "Voltage of 1V5", "boards.gdx1.sensors.ID_17.value"),
                    ("gdx_volt_0V75_VREF", "Voltage of 0V75_VREF", "boards.gdx1.sensors.ID_18.value"),
                #OS Board
                    #Temperatures
                    ("os_temp_1", "acpitz-virtual-0::temp1", "boards.os.sensors.ID_9.value"),
                    ("os_temp_2", "coretemp-isa-0000::Core 0", "boards.os.sensors.ID_10.value"),                        
                ]