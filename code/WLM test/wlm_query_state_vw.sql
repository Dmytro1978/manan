CREATE OR REPLACE VIEW "public" ."wlm_query_state_vw"
AS
SELECT stv_wlm_query_state.query,
       stv_wlm_query_state.service_class - 5 AS queue,
       stv_wlm_query_state.slot_count,
       BTRIM(stv_wlm_query_state.wlm_start_time::CHARACTER VARYING::TEXT) AS start_time,
       BTRIM(stv_wlm_query_state.state::CHARACTER VARYING::TEXT) AS state,
       BTRIM(stv_wlm_query_state.queue_time::CHARACTER VARYING::TEXT) AS queue_time,
       BTRIM(stv_wlm_query_state.exec_time::CHARACTER VARYING::TEXT) AS exec_time
FROM stv_wlm_query_state


