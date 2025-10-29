select c.id as id, c.genotype as genotype, p.genotype as parent_genotype
from ecoli_data as p
join ecoli_data as c
on p.id = c.parent_id
having p.genotype & c.genotype = p.genotype
order by id