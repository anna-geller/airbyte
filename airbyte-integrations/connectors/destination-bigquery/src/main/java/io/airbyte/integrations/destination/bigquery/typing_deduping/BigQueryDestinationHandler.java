package io.airbyte.integrations.destination.bigquery.typing_deduping;

import com.google.cloud.bigquery.BigQuery;
import com.google.cloud.bigquery.QueryJobConfiguration;
import com.google.cloud.bigquery.Table;
import com.google.cloud.bigquery.TableDefinition;
import io.airbyte.integrations.destination.bigquery.typing_deduping.SqlGenerator.StreamId;
import java.util.Optional;
import java.util.UUID;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

// TODO this stuff almost definitely exists somewhere else in our codebase.
public class BigQueryDestinationHandler implements DestinationHandler<TableDefinition> {

  private static final Logger LOGGER = LoggerFactory.getLogger(BigQueryDestinationHandler.class);

  private final BigQuery bq;

  public BigQueryDestinationHandler(final BigQuery bq) {
    this.bq = bq;
  }

  @Override
  public Optional<TableDefinition> findExistingTable(StreamId id) {
    final Table table = bq.getTable(id.finalNamespace(), id.finalName());
    return Optional.ofNullable(table).map(Table::getDefinition);
  }

  @Override
  public void execute(final String sql) throws InterruptedException {
    if ("".equals(sql)) {
      return;
    }
    final UUID queryId = UUID.randomUUID();
    LOGGER.info("Executing sql {}: {}", queryId, sql);
    long start = System.currentTimeMillis();
    bq.query(QueryJobConfiguration.newBuilder(sql).build());
    LOGGER.info("Completed sql {} in {} ms", queryId, System.currentTimeMillis() - start);
  }
}
